import streamlit as st
import torch
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings,HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from langchain.chains import ConversationalRetrievalChain

from htmlTemplates import css, bot_template, user_template
from langchain_community.embeddings import HuggingFaceInstructEmbeddings, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain.llms import HuggingFaceHub



def get_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks




def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    if not embeddings:
        print("Embeddings list is empty. Cannot proceed with FAISS.from_texts.")
        return None
    try:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings).to(device)
    except RuntimeError as e:
        if "CUDA out of memory" in str(e):
            print("CUDA out of memory. Moving computation to CPU.")
            device = torch.device("cpu")
            vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings).to(device)
        else:
            raise e
    return vectorstore


def get_conversation_chain(vectorstore):
   
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":50})
    llm = HuggingFaceHub(repo_id="mrm8488/t5-small-finetuned-quora-question-answering", model_kwargs={"temperature": 0.5, "max_length": 50})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain



def handle_userinput(user_question):
    if st.session_state.conversation is None:
        # If conversation is not initialized, initialize it here
        vectorstore = st.session_state.vectorstore
        if vectorstore is not None:
            st.session_state.conversation = get_conversation_chain(vectorstore)
        else:
            st.write("Error: Vector store not initialized.")
            return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)





def main():
    load_dotenv()
    st.set_page_config(page_title="ask your doc",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)


if __name__ == '__main__':
    main()
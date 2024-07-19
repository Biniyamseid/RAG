# Retrieval-Augmented Generations

![GitHub stars](https://img.shields.io/github/stars/yourusername/Chat-with-pdf-LLM-application?style=social) ![GitHub forks](https://img.shields.io/github/forks/yourusername/Chat-with-pdf-LLM-application?style=social) ![GitHub issues](https://img.shields.io/github/issues/yourusername/Chat-with-pdf-LLM-application) ![Python version](https://img.shields.io/badge/python-3.8+-blue.svg)

![RAG Application](image.png)


The Chat-with-pdf-LLM-application is designed to enhance your productivity by allowing seamless interaction with PDF documents through a conversational interface. This application leverages the latest advancements in language learning models to revolutionize how you engage with digital documents.

## Features

- Interactive Chat Interface
- Advanced Search within PDFs
- Summarization of documents

## Installation

To install the Chat-with-pdf-LLM-application, please follow these steps:


sudo apt-get update
pip install tf-keras
sudo apt-get install swig

1. **Clone the repository** to your local machine.


   ```bash
   git clone https://github.com/Biniyamseid/RAG.git
   ```
   ```
   cd RAG
   ```

   1. Install the required dependencies by running the following command:

 ```
   pip install -r requirements.txt
   ```

2 . Run the main.py file using the Streamlit CLI. Execute the following command:

```
   streamlit run app.py
   ```
   or

```
   python3 -m streamlit run app.py
   ```



## Dependencies and Their Usage in Building RAG

In the development of RAG, several key libraries and frameworks were utilized to ensure its functionality and performance. Below is a list of these dependencies along with their specific usage in the project:

- **langchain (0.0.184):** Used for integrating language models with chain-of-thought reasoning capabilities, enhancing the natural language understanding and generation aspects of RAG.

- **PyPDF2 (3.0.1):** Employed for handling PDF file manipulations, such as reading and extracting text, which is crucial for processing source documents in RAG.

- **python-dotenv (1.0.0):** Facilitates the loading of environment variables from a `.env` file, which is essential for managing configuration and sensitive information securely.

- **streamlit (1.18.1):** Provides an easy-to-use framework for building interactive web applications. In RAG, Streamlit is used to create the user interface that allows users to interact with the model and view results.

- **openai (0.27.6):** The OpenAI library is used to integrate GPT models for generating text and performing various NLP tasks, contributing to the model's ability to understand and generate human-like text.

- **faiss-cpu (1.7.4):** A library for efficient similarity search and clustering of dense vectors. In RAG, FAISS is used to quickly retrieve relevant documents from a large corpus, enhancing the retrieval-augmented generation process.

- **altair (4):** A declarative statistical visualization library for Python. Altair is used in RAG for creating interactive charts and visualizations to analyze and present data effectively.

- **tiktoken (0.4.0):** Utilized for tokenization and preprocessing of text data, ensuring that input data is in the correct format for processing by the model.

- **InstructorEmbedding (1.0.1):** A custom library for creating and managing embeddings, used in RAG to enhance the understanding of complex queries and documents through vector representations.

- **sentence-transformers (2.2.2):** Leveraged for generating sentence embeddings, which are crucial for semantic search and similarity comparisons in the retrieval component of RAG.

These dependencies are integral to the functionality and performance of RAG, each contributing to different aspects of the system, from data processing and model interaction to user interface design and visualization.



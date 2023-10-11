import os

from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.docstore.document import Document

import csv
from langchain.docstore.document import Document

from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings




huggingfacehub_api_token = os.environ['HUGGINGFACEHUB_API_TOKEN']
repo_id = "meta-llama/Llama-2-7b"





def load_text_from_csv_files(directory_path):
    documents = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            # Load data from a CSV file
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    text = ' '.join(row)
                    document = Document(text)
                    documents.append(document)

    return documents

directory_path = './new_papers/'  # Replace with your directory path
loaded_documents = load_text_from_csv_files(directory_path)


# Initialize your model
chatbot = ChatGPT.from_pretrained("model_name")
embeddings = YourEmbeddings()

# Initialize other components such as Langchain, Chainlit, etc.

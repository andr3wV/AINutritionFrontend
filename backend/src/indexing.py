# Indexing a document 

# Offline component of RAG pipeline.

import glob 
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from sentence_transformers import SentenceTransformer
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

from vectorstore import VECTOR_STORE, drop_collection

# import pad_fields, rename_fields()

PDF_GLOB = "/Users/ryanfryer/Documents/VS Code/LLM_ASSIGNMENT_WALKTHROUGH_BOILERPLATE/PDFs/12 Common Food Additives — Should You Avoid Them?.pdf" # File Path Name
pdf_files = glob.glob(PDF_GLOB)
pdf_docs = [PyPDFLoader(file).load()[0] for file in pdf_files]
print(f"Loaded {len(pdf_docs)}")

load_dotenv()

# URL_FILE = "web_urls.txt" # The source path of your text documents with links you want.

# web_urls = open(URL_FILE).readlines()
# web_urls = [url.strip() for url in web_urls if len(url.strip() > 0)]
# web_docs = WebBaseLoader(web_paths=web_urls).load()
# print(f"Loaded {len(web_docs)} documents")

# all_documents = pdf_docs + web_docs
all_documents = pdf_docs
print(f"Loaded {len(all_documents)} documents")

# This section will chunk our documents now that they are loaded.

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(all_documents)
print(f"Split {len(chunks)} text chunks")

for chunk in chunks:
    print(chunk)

listOfEmbeddings = []
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=os.getenv("API_KEY"))
listOfEmbeddings.append(embeddings.embed_query("Hello!"))

print(listOfEmbeddings[0])

# Installing the sentence transformer model to get the sentence into a higher 
# dimensional vector space of 768 dimensions. This dimension space will help us to better 
# query the vector database for sentences that better match what we are looking for.
    
# model = SentenceTransformer('sentence-transformers/quora-distilbert-multilingual')
# embeddings = model.encode(chunks)
# print(embeddings[1])



# This section creates the vector databse we will be using here.

# Milvus is the name of the vector database we will use here.

drop_collection()
added = VECTOR_STORE.add_documents(chunks)
print(f"Added {len(added)} text chunks to the vector store")



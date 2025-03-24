from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

_API_KEY = os.getenv("API_KEY")
_MODEL = "text-embedding-3-large"

EMBEDDINGS = OpenAIEmbeddings(model=_MODEL, api_key=_API_KEY)
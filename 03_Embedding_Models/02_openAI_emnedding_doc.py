from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32
)

documents = [
    "Project AVA is an AI-powered assistant developed by Razer.",
    "Razer is a global gaming lifestyle brand.",
    "Razer manufactures gaming laptops, keyboards, mice, and headsets.",
    "Artificial Intelligence improves gaming experiences.",
    "LangChain helps developers build applications using Large Language Models."
]

result = embedding.embed_documents(document)

print(str(result))
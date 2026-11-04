
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    output_dimensionality=32
)

documents = [
    "Project AVA is an AI-powered assistant developed by Razer.",
    "Razer is a global gaming lifestyle brand.",
    "Razer manufactures gaming laptops, keyboards, mice, and headsets.",
    "Artificial Intelligence improves gaming experiences.",
    "LangChain helps developers build applications using Large Language Models."
]

result = embedding.embed_documents(documents)

print(result)
print("Number of embeddings:", len(result))


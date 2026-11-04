from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
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

query = "What are the other products Razer manufactures"

doc_embedding = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)

# print(doc_embedding,len(doc_embedding))
# print("_"*50)
# print(query_embedding,len(query_embedding))

similarity_score = cosine_similarity([query_embedding],doc_embedding)[0]

result = max(enumerate(similarity_score),key=lambda x:x[1])
print(query)
print(documents[result[0]])
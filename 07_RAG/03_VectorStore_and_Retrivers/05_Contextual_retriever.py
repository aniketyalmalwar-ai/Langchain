# Maximum marginal retriver

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_google_genai import ChatGoogleGenerativeAI
documents = [
    Document(
        page_content="""
        Cricket is one of the most popular sports in India.
        The Indian cricket team has won multiple international tournaments.
        Sachin Tendulkar is widely regarded as one of the greatest batsmen.
        The game is played in formats such as Test, ODI, and T20.
        """,
        metadata={"topic": "Cricket", "category": "Sports"}
    ),

    Document(
        page_content="""
        Python is a high-level programming language known for its simplicity.
        It supports object-oriented, functional, and procedural programming.
        Python is widely used in artificial intelligence, machine learning,
        web development, automation, and data science.
        Popular frameworks include Django, Flask, FastAPI, and LangChain.
        """,
        metadata={"topic": "Python", "category": "Programming"}
    ),

    Document(
        page_content="""
        The solar system consists of the Sun and all celestial objects
        gravitationally bound to it. There are eight recognized planets.
        Earth is the only planet currently known to support life.
        Jupiter is the largest planet, while Mercury is the smallest.
        """,
        metadata={"topic": "Solar System", "category": "Science"}
    ),

    Document(
        page_content="""
        Artificial Intelligence enables machines to perform tasks
        that traditionally require human intelligence.
        Machine learning allows systems to learn patterns from data.
        Deep learning uses neural networks with multiple layers.
        Generative AI can create text, images, audio, and code.
        """,
        metadata={"topic": "Artificial Intelligence", "category": "Technology"}
    ),

    Document(
        page_content="""
        The Indian economy is one of the largest economies in the world.
        Agriculture, manufacturing, and services contribute to its GDP.
        The Reserve Bank of India manages monetary policy.
        Digital payments such as UPI have transformed financial transactions.
        """,
        metadata={"topic": "Indian Economy", "category": "Economics"}
    )
]

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorStore  = FAISS.from_documents(
    documents=documents,
    embedding= embedding_model,
)

base_retriver = vectorStore.as_retriever(search_kwargs={'k':2})
compresser  = LLMChainExtractor.from_llm(llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite"))

retriver = ContextualCompressionRetriever(
    base_retriever=base_retriver,
    base_compressor=compresser
)

query = "tell me about cricket"
result = retriver.invoke(query)

for i,doc in enumerate(result,start=1):
    print(f"Result{i}")
    print(doc.page_content)

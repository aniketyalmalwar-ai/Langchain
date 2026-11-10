import wikipedia
from langchain_community.retrievers import WikipediaRetriever

wikipedia.set_user_agent(
    "Aniket/1.0"
)

retriver = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "History of cricket"

docs = retriver.invoke(query)

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}")
    print("Content:", doc.page_content)

import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://en.wikipedia.org/wiki/Cricket"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.get_text(strip=True) if soup.title else "Unknown"

for element in soup(["script", "style", "nav", "footer", "header"]):
    element.decompose()

text_data = soup.get_text(separator="\n", strip=True)

docs = Document(
    page_content=text_data,
    metadata={
        "source": url,
        "title": title,
        "file_type": "webpage"
    }
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)
prompt = PromptTemplate(
    template="Summarize the following website content in 250 characters:\n{text}",
    input_variables=["text"]
)
parser = StrOutputParser()
chain = prompt | model | parser
result = chain.invoke({"text": docs.page_content[:15000]})

print(result)

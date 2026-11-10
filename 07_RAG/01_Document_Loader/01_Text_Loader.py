from pathlib import Path
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash-lite'
)

BASE_DIR = Path(__file__).resolve().parent

file_path = BASE_DIR.parent / "Data" / "Cricket.txt"

text = file_path.read_text(encoding="utf-8")

docs = Document(
    page_content=text,
    metadata={
        'author':'Aniket',
        'file-name':file_path.name,
        'file-type':file_path.suffix
    }
)

prompt = PromptTemplate(
    template="Summarize the given text in 250 characters../n{text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)
result= chain.invoke({'text':docs.page_content})
print(result)


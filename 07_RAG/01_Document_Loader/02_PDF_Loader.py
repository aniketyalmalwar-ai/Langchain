from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH.parent /"Data"/"Cricket.pdf"

model  =ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

reader = PdfReader(str(file_path))

text = "\n".join(page.extract_text() or " " for page in reader.pages)

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
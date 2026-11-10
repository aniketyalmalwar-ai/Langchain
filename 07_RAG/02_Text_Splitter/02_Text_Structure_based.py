from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH.parent /"Data"/"Cricket.pdf"

reader = PdfReader(file_path)

text = "\n".join(page.extract_text() or "" for page in reader.pages)

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 50,
    chunk_overlap = 0,
)

result = splitter.split_text(text)

print(result)
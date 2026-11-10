from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH.parent /"Data"/"Cricket.py"

text =file_path.read_text(encoding='utf-8')

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 500,
    chunk_overlap=0
)

Result = splitter.split_text(text)

print(Result)
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH.parent /"Data"/"Cricket.md"

text =file_path.read_text(encoding='utf-8')

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size = 500,
    chunk_overlap=0
)

Result = splitter.split_text(text)

print(Result)
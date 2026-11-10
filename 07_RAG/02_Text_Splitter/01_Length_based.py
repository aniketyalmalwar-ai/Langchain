from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

BASE_PATH = Path(__file__).resolve().parent

file_path = BASE_PATH.parent /"Data"/"Cricket.txt"
text = file_path.read_text(encoding="utf-8")

docs = Document(
    page_content=text,
    metadata={
        'Author':'Aniket Y',
        'FileName':file_path.name,
        'FileType':file_path.suffix
    }
)

splitter = CharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=0,
    separator=' '
)

result = splitter.split_text(docs.page_content)

print(result)
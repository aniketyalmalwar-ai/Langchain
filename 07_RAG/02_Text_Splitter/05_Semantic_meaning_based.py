
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH.parent / "Data" / "mixed_content.txt"

text = file_path.read_text(encoding="utf-8")

doc = Document(
    page_content=text,
    metadata={
        "Author": "Aniket Y",
        "FileName": file_path.name,
        "FileType": file_path.suffix
    }
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95,
    buffer_size=0
)

result = splitter.split_documents([doc])

for i, chunk in enumerate(result, start=1):
    print(f"\n{'_' * 50}")
    print(chunk.page_content)

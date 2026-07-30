from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import Docx2txtLoader

DOCUMENTS_DIR = Path("data/docs")

loader = DirectoryLoader(
    DOCUMENTS_DIR,
    glob="*.docx",
    loader_cls=Docx2txtLoader,
)

documents = loader.load()

print(f"\nLoaded {len(documents)} document(s)\n")

print("=" * 80)
print(documents[0].page_content)
print("=" * 80)
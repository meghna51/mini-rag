"""Step 1: read text files, split into chunks, store them in a ChromaDB vector database."""
from pathlib import Path

import chromadb

DOCS_DIR = "docs"          # put your .md / .txt files here
DB_DIR = "chroma_db"       # where the vector database is saved
CHUNK_SIZE = 500           # characters per chunk
OVERLAP = 100              # characters shared between neighbouring chunks


def split_text(text):
    """Cut text into overlapping pieces so ideas aren't lost at the boundaries."""
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + CHUNK_SIZE])
        start += CHUNK_SIZE - OVERLAP
    return chunks


def main():
    client = chromadb.PersistentClient(path=DB_DIR)
    # Chroma turns each chunk into an embedding (a vector of numbers) automatically.
    try:
        client.delete_collection("docs")
    except Exception:
        pass
    collection = client.create_collection("docs")

    ids, texts, metas = [], [], []
    for path in Path(DOCS_DIR).glob("*"):
        if path.suffix not in {".md", ".txt"}:
            continue
        for i, chunk in enumerate(split_text(path.read_text(encoding="utf-8"))):
            ids.append(f"{path.name}-{i}")
            texts.append(chunk)
            metas.append({"source": path.name})

    if not texts:
        raise SystemExit(f"No .md or .txt files found in '{DOCS_DIR}/'.")
    collection.add(ids=ids, documents=texts, metadatas=metas)
    print(f"Stored {len(texts)} chunks in '{DB_DIR}'.")


if __name__ == "__main__":
    main()

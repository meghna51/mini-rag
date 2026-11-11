"""Step 2: find the chunks most similar to a question, then let Claude answer using only them."""
import sys

import anthropic
import chromadb
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from the .env file

DB_DIR = "chroma_db"
TOP_K = 3                  # how many chunks to retrieve
MODEL = "claude-sonnet-4-5"


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python ask.py "your question"')
    question = sys.argv[1]

    # 1. RETRIEVE: vector search for the most similar chunks
    collection = chromadb.PersistentClient(path=DB_DIR).get_collection("docs")
    results = collection.query(query_texts=[question], n_results=TOP_K)
    chunks = results["documents"][0]
    sources = {m["source"] for m in results["metadatas"][0]}

    # 2. AUGMENT: put those chunks into the prompt
    context = "\n\n---\n\n".join(chunks)
    prompt = (
        "Answer the question using ONLY the context below. "
        "If the answer is not in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )

    # 3. GENERATE: ask the LLM
    reply = anthropic.Anthropic().messages.create(
        model=MODEL, max_tokens=500, messages=[{"role": "user", "content": prompt}]
    )
    print(reply.content[0].text)
    print("\nSources:", ", ".join(sorted(sources)))


if __name__ == "__main__":
    main()

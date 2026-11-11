# Mini RAG: Ask Questions About Your Documents

A small Retrieval-Augmented Generation (RAG) app in two scripts (~70 lines total).
It splits your documents into chunks, stores them in a vector database (ChromaDB),
finds the chunks most relevant to a question, and has an LLM (Claude) answer using only those chunks.

## How it works
```
ingest.py:  files -> chunks -> embeddings -> ChromaDB
ask.py:     question -> similar chunks -> prompt -> Claude -> answer + sources
```

## Run it
```bash
pip install -r requirements.txt
cp .env.example .env          # add your Anthropic API key
                              # docs/ already has a sample file; add your own .md / .txt files
python ingest.py
python ask.py "Why does chunking matter?"
```

## 7-day learning plan (about 1 hour a day)
| Day | Goal | What to do |
|-----|------|-----------|
| 1 | Understand RAG | Read the diagram above. Explain in your own words: why not paste the whole document into the prompt? |
| 2 | Chunking | Read `split_text`. Change CHUNK_SIZE / OVERLAP, re-run `ingest.py`, see how answers change. |
| 3 | Embeddings | Learn that an embedding is a list of numbers capturing meaning. Query Chroma directly in a Python shell and print distances. |
| 4 | Vector DB | Read the ChromaDB docs for `add` and `query`. Add a metadata filter (e.g. only one source file). |
| 5 | The LLM step | Read the prompt in `ask.py`. Try removing "ONLY" and see hallucinations. Try asking something not in the docs. |
| 6 | Make it yours | Use your own documents (notes, a handbook, papers). Add one feature: PDF support with `pypdf`, or a `--top-k` argument. |
| 7 | Package it | Write a README with a screenshot, push to GitHub, and practise a 2-minute explanation. |

## Interview questions you should be able to answer
- What is an embedding, and how does similarity search work?
- Why chunk documents, and why use overlap?
- What happens if retrieval returns the wrong chunks?
- How does RAG reduce hallucination, and where can it still fail?
- How would you evaluate it? (Make 20 questions with known answers and check if the right chunk is retrieved.)

## Resume bullet (adjust to what you really did)
- Built a Retrieval-Augmented Generation app in Python using ChromaDB for vector search and the Claude API
  to answer questions grounded in a custom document set, returning source file references.

## Next steps once comfortable
Add PDF loading, a Streamlit chat UI, then hybrid search (BM25 + vectors) and an evaluation script.

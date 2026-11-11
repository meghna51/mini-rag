# About Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is a technique that gives a language model access to
external knowledge at question time. Instead of relying only on what the model learned
during training, a RAG system first searches a collection of documents for passages that
are relevant to the question, and then includes those passages in the prompt.

## Why chunking matters

Documents are split into smaller chunks before they are stored. Chunks that are too large
dilute the meaning and waste prompt space. Chunks that are too small lose context. Using a
small overlap between neighbouring chunks helps keep ideas intact across boundaries.

## Embeddings and vector databases

An embedding is a list of numbers that represents the meaning of a piece of text. Texts with
similar meaning have embeddings that are close together. A vector database such as ChromaDB
stores these embeddings and can quickly find the ones closest to a query embedding.

## Reducing hallucination

Telling the model to answer only from the provided context, and to say it does not know when
the context is insufficient, reduces made-up answers. Returning the source file for each
answer lets users verify the information themselves.

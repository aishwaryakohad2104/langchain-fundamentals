INTENT_PROMPT = """
Classify the user query into one of the following categories:
- rag
- summary
- compare

Only return one word.
Query: {question}
"""

RAG_PROMPT = """
Answer the question using the context below.

Context:
{context}

Question:
{question}
"""

SUMMARY_PROMPT = """
Provide a concise summary of the following text:

{text}
"""

COMPARE_PROMPT = """
Compare key arguments and insights from the following text:

{text}
"""
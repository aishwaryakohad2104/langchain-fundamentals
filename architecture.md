User Question
     ↓
Intent Classifier (LangGraph Node)
     ↓
 ┌───────────────┬───────────────┬───────────────┐
 │ RAG Node      │ Summary Node  │ Compare Node  │
 └───────────────┴───────────────┴───────────────┘
     ↓
Final Answer



RAG Pipeline:

Document loading
Chunking
Embeddings
Vector store
RetrievalQA chain

PDF → Split → Embed → Store → Retrieve → LLM → Answer

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from config.settings import MODEL_NAME, EMBEDDING_MODEL

def get_llm():
    return ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
        )

def get_embeddings():
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)
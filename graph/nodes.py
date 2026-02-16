from llm.llm import get_llm
from utils.prompts import INTENT_PROMPT, RAG_PROMPT, SUMMARY_PROMPT, COMPARE_PROMPT

llm = get_llm()

def classify_intent(state):
    prompt = INTENT_PROMPT.format(question=state['question'])
    response = llm.invoke(prompt)
    intent = response.content.strip().lower()
    return {"intent": intent}

def rag_node(state):
    retriever = state["vectorstore"].as_retriever()
    documents = retriever.get_relevant_documents(state["question"])

    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = RAG_PROMPT.format(question=state['question'], context=context) 
    response = llm.invoke(prompt)
    return {"answer": response.content}

def summary_node(state):
    retriever = state["vectorstore"].as_retriever()
    documents = retriever.get_relevant_documents(state["question"])

    text = "\n\n".join([doc.page_content for doc in documents])

    prompt = SUMMARY_PROMPT.format(text=text)
    response = llm.invoke(prompt)

    return {"answer": response.content}

def compare_node(state):
    retriever = state["vectorstore"].as_retriever()
    documents = retriever.get_relevant_documents(state["question"])

    text = "\n\n".join([doc.page_content for doc in documents])

    prompt = COMPARE_PROMPT.format(question=state['question'], text=text)
    response = llm.invoke(prompt)

    return {"answer": response.content}
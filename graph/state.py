from typing import TypedDict, List, Optional

class GraphState(TypedDict):
    question: str
    intent: str
    documents: List[str]
    answer: str
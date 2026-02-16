from langgraph.graph import StateGraph
from graph.state import GraphState
from graph.nodes import classify_intent, rag_node, summary_node, compare_node

def build_graph():

    workflow = StateGraph(GraphState)

    workflow.add_node("classifier",classify_intent)
    workflow.add_node("rag", rag_node)
    workflow.add_node("summary", summary_node)
    workflow.add_node("compare", compare_node)

    workflow.set_entry_point("classifier")

    def route(state):
        return state["intent"]
    
    workflow.add_conditional_edges(
        "classifier",
        route,
        {
            "rag": "rag",
            "summary": "summary",
            "compare": "compare"
        }
    )

    workflow.set_finish_points(["rag", "summary", "compare"])

    return workflow.compile()
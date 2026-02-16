from vectorstore.build_vectorstore import build_vectorstore
from graph.workflow import build_graph

def main():
    # Step 1: Build the vector store
    vectorstore = build_vectorstore()

    # Step 2: Build the workflow graph
    app = build_graph()

    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        result = app.invoke({
            "question": question,
            "vectorstore": vectorstore
        }
        )

        print("\nAnswer:\n")
        print(result["answer"])

if __name__ == "__main__":
    main()
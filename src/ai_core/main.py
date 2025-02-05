from ai_core.graph import graph
from ai_core.utils import run_graph_sync, visualize_graph

# Visualize graph
visualize_graph(graph)

# Run graph
input = input("Enter your query: ")
result = run_graph_sync(graph, {"messages": [{"role": "user", "content": input}]})
messages = result["messages"]

for message in messages:
    print(message)
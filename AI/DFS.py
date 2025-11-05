def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)

# Taking user input
edges = int(input("Enter number of edges: "))
graph = {}

print("Enter edges (format: node1 node2):")
for _ in range(edges):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # For undirected graph

start_node = input("Enter the starting node for DFS: ")
visited = set()
print("DFS traversal:")
dfs(graph, start_node, visited)

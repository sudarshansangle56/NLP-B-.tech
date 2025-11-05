from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result


graph = defaultdict(list)

n = int(input("Enter number of edges: "))
print("Enter edges (format: node1 node2):")
for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  

start_node = int(input("Enter the starting node for BFS: "))

bfs_result = bfs(graph, start_node)


print("BFS Traversal:", ' -> '.join(map(str, bfs_result)))

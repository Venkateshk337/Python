def BFS(graph, visited, start):
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


v = int(input("Enter the number of vertices:"))
graph = [[] for _ in range(v)]
visited = [False] * v

E = int(input("Enter the number of Edges:"))
for i in range(E):
    print(f"Enter edge {i + 1} separated by spaces:")
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print("\nAdjacency list:")
for i in range(v):
    print(f"{i}:{graph[i]}")

start = int(input("Enter starting vertex:"))
print("\nBFS")

BFS(graph, visited, start)
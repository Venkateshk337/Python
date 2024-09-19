def DFS(graph, visited, vertex):
    visited[vertex] = True
    print(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            DFS(graph, visited, neighbor)


V = int(input("\nEnter number of vertices: "))
graph = {}
visited = [False] * V

E = int(input("\nEnter number of edges: "))
for i in range(E):
    print(f"Enter edge {i + 1} separated by spaces: ")
    u=input("Enter the edge separated by space:")
    if u[0] not in graph:
        graph.update(u[0], [])
    if u[1] not in graph:
        graph.update(u[1], [])
    graph[u[0]].ap




print("\nAdjacency list: ")
for i in range(V):
    print(f"{i}: {graph[i]}")

start = int(input("\nEnter starting vertex: "))
print("\nDFS: ")
DFS(graph, visited, start)

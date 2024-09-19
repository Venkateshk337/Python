# import heapq
#
#
# def dijkstra(graph, start):
#     # Priority queue to store (cost, vertex) tuples
#     pq = []
#     heapq.heappush(pq, (0, start))
#
#     # Dictionary to store the shortest path to each vertex
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#
#     while pq:
#         current_distance, current_vertex = heapq.heappop(pq)
#
#         # Nodes can only be added to the priority queue once, so we can skip these checks
#         if current_distance > distances[current_vertex]:
#             continue
#
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#
#             # Only consider this new path if it's better
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#
#     return distances
#
#
# def main():
#     # Read the number of vertices
#     num_vertices = int(input("Enter the number of vertices: "))
#
#     # Read the vertices
#     graph = {}
#     for _ in range(num_vertices):
#         vertex = input("Enter the vertex: ")
#         graph[vertex] = {}
#
#     # Read the number of edges
#     num_edges = int(input("Enter the number of edges: "))
#
#     # Read the edges
#     for _ in range(num_edges):
#         u = input("Enter the start vertex of the edge: ")
#         v = input("Enter the end vertex of the edge: ")
#         weight = int(input("Enter the weight of the edge: "))
#         if u in graph:
#             graph[u][v] = weight
#         else:
#             graph[u] = {v: weight}
#
#     # Read the start vertex
#     start_vertex = input("Enter the start vertex: ")
#
#     # Run Dijkstra's algorithm
#     distances = dijkstra(graph, start_vertex)
#
#     # Print the results
#     print(f"\nShortest distances from node {start_vertex}:")
#     for vertex in distances:
#         print(f"Distance to {vertex}: {distances[vertex]}")
#
#
# if __name__ == "__main__":
#     main()


def dijkstra(graph, start):
    distances = {node: 999 for node in graph}
    distances[start] = 0
    unvisited = set(graph.keys())
    while unvisited:
        current_node = min(unvisited, key=distances.get)
        unvisited.remove(current_node)
        for neighbure, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbure]:
                distances[neighbure] = distance
    return distances

# Take user inputs to build the graph
graph = {}  # dictionary
n = int(input("Enter the number of edges: "))

for _ in range(n):
    source, destination, weight = input("Enter an edge (source destination weight): ").split()
    weight = int(weight)

    if source not in graph:
        graph[source] = {}
    if destination not in graph:
        graph[destination] = {}

    graph[source][destination] = weight
    graph[destination][source] = weight

# Take user input for the starting node
start_node = input("Enter the starting node: ")
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node + ":")
for node, distance in distances.items():
    print("Node:", node, "Distance:", distance)

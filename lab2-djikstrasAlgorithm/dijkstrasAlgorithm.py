# Declaring the graph using an adjacency matrix
vertices = 9
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]

# Taking input of start vertex
while True:
    print("Enter start vertex: ", end="")
    start = int(input())
    if start > vertices - 1:
        print("vertex " + str(start) + " is not in the graph")
    else:
        break

# dist contains the minimum distances of each node from the start node
dist = [99999] * vertices
# distance of start node will be 0
dist[start] = 0
# sptSet is the set of all vertices which have been included in the shortest path tree
sptSet = [False] * vertices

for _ in range(vertices):

    min = 99999
    # finding the node with the minimum distance from the start node which is not
    # already in the shortest path tree
    for v in range(vertices):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    u = min_index

    # adding the node with the minimum distance to the shortest path tree
    sptSet[u] = True

    # Updating the values of all adjacent nodes
    for v in range(vertices):
        if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
            dist[v] = dist[u] + graph[u][v]

print("Vertex \tDistance from source vertex " + str(start))
for node in range(vertices):
    print(node, "\t", dist[node])

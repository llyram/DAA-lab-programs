#!/bin/python

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


key = [99999] * vertices
parent = [None] * vertices
key[0] = 0
mstSet = [False] * vertices # vertices included in the MST
parent[0] = -1

for cout in range(vertices):
    min = 999999
    for v in range(vertices):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    u = min_index
    mstSet[u] = True
    for v in range(vertices):
        if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
            key[v] = graph[u][v]
            parent[v] = u


# Print the MST
total_weight = 0
print("Edge \tWeight")
for i in range(1, vertices):
    print(parent[i], "-", i, "\t", graph[i][parent[i]])
    total_weight += graph[i][parent[i]]

print("minimum weight : " + str(total_weight))

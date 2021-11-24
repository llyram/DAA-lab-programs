#!/bin/python

graph = [[0, 1, 4], [0, 7, 8], [1, 7, 11], [1, 2, 8], [8, 2, 2], [7, 8, 7], [2, 3, 7], [
    7, 6, 1], [8, 6, 6], [2, 5, 4], [6, 5, 2], [3, 5, 14], [3, 4, 9], [5, 4, 10]]
vertices = 9


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


result = []
i = 0
e = 0

# Sort the graph according to weight of each edge
graph = sorted(graph, key=lambda item: item[2])

parent = [i for i in range(vertices)]
rank = [0] * vertices

while e < vertices - 1:

    u, v, w = graph[i]
    i += 1
    x = find(parent, u)
    y = find(parent, v)

    if x != y:
        e += 1
        result.append([u, v, w])
        union(parent, rank, x, y)

total_weight = 0
print("Edges\tWeight")
for u, v, weight in result:
    print("%d - %d\t%d" % (u, v, weight))
    total_weight += weight

print("minimum weight : " + str(total_weight))

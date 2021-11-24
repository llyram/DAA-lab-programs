#!/bin/python

V = 4

INF = 99999

def floydWarshall(graph):

    dist = graph

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)

def printSolution(dist):
    print(graph_diagram)
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("INF\t", end="")
            else:
                print(dist[i][j], "\t", end=""),
            if j == V-1:
                print("")

graph_diagram = """
            10
       (0)------->(3)
        |         /|\\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           """

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
         
floydWarshall(graph)
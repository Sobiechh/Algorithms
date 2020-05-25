import networkx as nx
import matplotlib.pyplot as plt


def backtrace(parent, start, end): #odwrocenie drogi
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def dijkstra(graph, source, target):
    queue = []
    visited = {}
    dist = {}
    shortest = {}
    parent = {}
    for i in range(len(graph)):
        dist[i] = None
        visited[i] = False
        parent[i] = None
        shortest[i] = float("inf")

    queue.append(source)
    dist[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True
        if current == target:
            print(backtrace(parent, source, target))

        for elem in graph[current]: #kazdy element z grafu
            if visited[elem] == False: #patrzymy czy nie przechodzilismy przez element
                dist[elem] = dist[current] + 1 
                if dist[elem] < shortest[elem]:
                    shortest[elem] = dist[elem]
                    parent[elem] = current
                    queue.append(elem)
    print(dist)  
    print(shortest)
    print(parent)
    print(target)

G = nx.Graph()
G.add_weighted_edges_from([(0, 1, 0), (1, 2, 1)]) #bilioteka network i uzycie add_eighter edges
dijkstra(G, 0, 2)
nx.draw(G) 
plt.show() #matplotlib do narysowania drogi

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
visited = set()


def dfs(visited, graph, vertice):
    if vertice not in visited:
        print(vertice)
        visited.add(vertice)
        for neighbour in graph[vertice]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, "A")

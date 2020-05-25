from collections import defaultdict #tylko do zrobienia dictionary

class BFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, u, v):
        self.graph[u].append(v)

    def algorytm(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = BFS()
g.add(0, 6)
g.add(0, 4)
g.add(4, 3)
g.add(3, 0)
g.add(3, 4)
g.algorytm(2)

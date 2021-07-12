from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph_dict = defaultdict(list)

    def addEdge(self, u, v):
        self.graph_dict[u].append(v)

    def dfs(self, visited, v):
        if v not in visited:
            print(v)
            visited.add(v)
            for n in self.graph_dict[v]:
                self.dfs(visited, n)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
visited = set()
print(g.graph_dict)
g.dfs(visited,  0)













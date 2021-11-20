import math


class Graph:
    def __init__(self, graph, source, sink):
        self.graph: list = graph
        self.number_of_lines = len(graph)
        self.source = source
        self.sink = sink

    def searching_algo_bfs(self, parent):
        queue = []
        visited = []

        for i in range(0, self.number_of_lines):
            visited.append(0)
        queue.append(self.source)
        visited[self.source] = True
        parent[self.source] = -1

        while len(queue) > 0:
            u = queue.pop(0)
            for v in range(0, self.number_of_lines):
                
                if visited[v] == False and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        if visited[self.sink]:
            return True
        else:
            return False

    def ford_fulkerson(self):
        max_flow: int = 0
        # батьківські елементи
        parent = [-1] * self.number_of_lines

        while self.searching_algo_bfs(parent):
            path_flow = math.inf
            v = self.sink

            while v != self.source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = parent[v]
            v = self.sink

            while v != self.source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            max_flow += path_flow

        return max_flow


if __name__ == '__main__':
    graph = [
        [0, 20, 10, 0, 0, 10],
        [0, 0, 0, 30, 0, 0],
        [0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0]
    ]
    g = Graph(graph, source=0, sink=5)
    print(f"Max Flow: {g.ford_fulkerson()}")

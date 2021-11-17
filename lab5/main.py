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
            vertical = queue.pop(0)
            for horizontal in range(0, self.number_of_lines):
                # якщо існує шлях між u та v, і він не відвіданий та його значеня більше 0
                if visited[horizontal] == False and self.graph[vertical][horizontal] > 0:
                    queue.append(horizontal)
                    visited[horizontal] = True
                    parent[horizontal] = vertical

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

            # пошук мінімального значення на шляху
            while v != self.source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = parent[v]
            v = self.sink

            # встановлює максимальний потік на шляху
            while v != self.source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            max_flow += path_flow

        return max_flow


if __name__ == '__main__':
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    g = Graph(graph, source=0, sink=5)
    print(f"Max Flow: {g.ford_fulkerson()}")

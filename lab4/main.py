def bfs(graph: dict, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        item = queue.pop(0)
        print(item, end=" ")

        if item not in graph:
            graph[item] = []
        for neighbour in graph[item]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {
        '0': ['1', '2'],
        '1': ['3', '4'],
        '2': ['5', '6'],
        '3': ['7', '8']
    }
    bfs(graph, '0')


def returnCurrencyPath(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        visited = set(path)
        for next in graph[vertex[0]] - visited:
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    graph = {
        'S': {('B', 2)},
        'B': {('C', 3), ('D', 1)},
        'C': {('F', 8), ('G', 1)},
        'D': {('E', 4), ('X', 10)},
        'E': {},
        'F': {},
        'G': {},
        'X': {}
    }

    path = next(returnCurrencyPath(graph, 'S', 'X'))
    path

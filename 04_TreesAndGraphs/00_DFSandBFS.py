###############################################################################
# Depth first (stack)
# https://eddmann.com/posts/
#   depth-first-search-and-breadth-first-search-in-python/
###############################################################################


def dfsRecursive(graph, start, visited=None):
    # Needs edge cases checks
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfsRecursive(graph, next, visited)
    return visited


def dfsIterative(graph, start, visited=None):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph[vertex]
            stack.extend(neighbors - visited)
    return visited


def dfsIterativePaths(graph, start, end):
    # Needs edge cases checks
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        visited = set(path)
        for next in graph[vertex] - visited:
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


###############################################################################
# Breadth first (queue)
# https://eddmann.com/posts/
#   depth-first-search-and-breadth-first-search-in-python/
###############################################################################


def bfsIterative(graph, start):
    visited, queue = set(), [start]
    while queue:
        probe = queue.pop(0)
        if probe not in visited:
            visited.add(probe)
            neighbors = graph[probe]
            queue.extend(neighbors-visited)
    return visited


def bfsIterativePaths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        visited = set(path)
        for next in graph[vertex] - visited:
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfsIterativePaths(graph, start, goal))
    except StopIteration:
        return None


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    dfsRecursive(graph, 'A')
    dfsIterative(graph, 'B')
    bfsIterative(graph, 'A')
    shortest_path(graph, 'A', 'E')

from numpy import true_divide


graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}


def haspath(graph, source, destination):
    if source == destination:
        return True
    for node in graph[source]:
        if haspath(graph, node, destination) == True:
            return True
    return False


# print(haspath(graph,'f','k'))


def haspath_b(graph, source, destination):
    if source == destination:
        return True
    queue = []
    queue.insert(0, source)
    while queue:
        current = queue.pop()
        for node in graph[current]:
            if node == destination:
                return True
            queue.insert(0, node)
            if node == destination:
                return True
    return False


print(haspath_b(graph, "f", "k"))

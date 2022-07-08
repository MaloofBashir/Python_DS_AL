from attr import has


edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]


def create_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


graph = create_graph(edges)
print(graph)


def haspath(graph, source, destination, visited=[]):
    if source == destination:
        return True
    if source in visited:
        return False
    visited.append(source)
    for node in graph[source]:
        if haspath(graph, node, destination, visited) == True:
            return True
    return False


print(haspath(graph, "i", "m"))

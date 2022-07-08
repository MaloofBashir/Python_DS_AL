graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def depth_first(graph, source):
    if source == "":
        return
    stack = []
    stack.append(source)
    while stack:
        current = stack.pop()
        print(current)
        for node in graph[current]:
            depth_first(graph, node)


depth_first(graph, "a")

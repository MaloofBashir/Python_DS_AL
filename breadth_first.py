import queue


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def breadth_first(graph, source):
    if source == "":
        return
    queue = []
    queue.insert(0, source)

    while queue:
        current = queue.pop()
        print(current)
        for node in graph[current]:
            queue.insert(0, node)


breadth_first(graph, "a")

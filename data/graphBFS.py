from collections import deque

graph = {
    "Alice":   ["Bob", "Charlie"],
    "Bob":     ["Alice", "Diana"],
    "Charlie": ["Alice", "Diana", "Eve"],
    "Diana":   ["Bob", "Charlie"],
    "Eve":     ["Charlie"]
}

def bfs(graph, start, target):
    queue = deque()
    visited = set()

    queue.append((start, 0))
    visited.add(start)

    while queue:
        node, steps = queue.popleft()

        if node == target:
            return node,steps

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, steps + 1))

    return -1

print(bfs(graph, "Alice", "Eve"))     # should be 2
print(bfs(graph, "Alice", "Diana"))   # should be 2
print(bfs(graph, "Alice", "Alice"))   # should be 0
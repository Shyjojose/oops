from collections import deque

graph = {
    "Alice":   ["Bob", "Charlie"],
    "Bob":     ["Alice", "Diana"],
    "Charlie": ["Alice", "Diana", "Eve"],
    "Diana":   ["Bob", "Charlie"],
    "Eve":     ["Charlie"]
}

def dfs(graph, start, target):
    stack = []          # ← stack not deque
    visited = set()
    stack.append((start, 0))
    visited.add(start)
    while stack:
        node, steps = stack.pop()    # ← pop() not popleft()

        if node == target:
            return node, steps

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append((neighbour, steps + 1))
    # your code here — stack not queue, pop() not popleft()

print(dfs(graph, "Alice", "Eve"))
print(dfs(graph, "Alice", "Diana"))
print(dfs(graph, "Alice", "Alice"))
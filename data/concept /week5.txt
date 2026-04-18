week 5 
tree is just a graph with one rule only on parent per node and no cycles And
remove the rule and you get graph. Node can connect to anything 
Alice ——— Bob
  |         |
Charlie — Diana
  |
 Eve

 Bfs is like we check direct friends first for Alice bob and charlie is the 
 first friends then we add diana and pop the first ones 

Data structure Qeue add this naturally 

Start: queue = [Alice]

Step 1: pop Alice → check her friends → add Bob, Charlie to queue
queue = [Bob, Charlie]

Step 2: pop Bob → check his friends → add Diana to queue
queue = [Charlie, Diana]

Step 3: pop Charlie → check his friends → add Diana, Eve to queue
queue = [Diana, Diana, Eve]   ← problem here — Diana twice

also need visited set to chect who has been visited to avoid visiting twice
graph = {
    "Alice":   ["Bob", "Charlie"],
    "Bob":     ["Alice", "Diana"],
    "Charlie": ["Alice", "Diana", "Eve"],
    "Diana":   ["Bob", "Charlie"],
    "Eve":     ["Charlie"]
}

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
    queue = append(start,0)# add start to queue
    visited= add.(start)# add start to visited
    while queue: # while queue has items:
     node, steps = queue.popleft()#     pop from front
    if node == target:  #     if it's the target → return steps
        return steps
    for neighbours in graph
        queue = append([start+1])#     add unvisited neighbours to queue
        visited = append.([start+1])#     mark them visited
    return -1   # not found

print(bfs(graph, "Alice", "Eve"))    # 2 steps — Alice→Charlie→Eve
print(bfs(graph, "Alice", "Diana"))  # 2 steps — Alice→Bob→Diana
print(bfs(graph, "Alice", "Alice"))  # 0 steps — already there

Start:  queue = [(Alice, 0)]   visited = {Alice}

Pop Alice (step 0)
  neighbours: Bob, Charlie
  queue = [(Bob,1), (Charlie,1)]
  visited = {Alice, Bob, Charlie}

Pop Bob (step 1) — not target
  neighbours: Alice✗, Diana
  queue = [(Charlie,1), (Diana,2)]
  visited = {Alice, Bob, Charlie, Diana}

Pop Charlie (step 1) — not target
  neighbours: Alice✗, Diana✗, Eve
  queue = [(Diana,2), (Eve,2)]
  visited = {Alice, Bob, Charlie, Diana, Eve}

Pop Diana (step 2) — not target
  neighbours: Bob✗, Charlie✗ — nothing to add

Pop Eve (step 2) — TARGET FOUND → return 2 ✅

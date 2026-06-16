# 🕸️ Graphs — Complete Reference Notes
> Extracted from Python DSA Mastery Notes — Week 5

---

## Table of Contents
1. [The Core Insight](#the-core-insight)
2. [How Multiple Keys are Stored in an Array](#how-multiple-keys-are-stored-in-an-array)
3. [Why We Need This in Programming](#why-we-need-this-in-programming)
4. [Graph Structure in Python](#graph-structure-in-python)
5. [Graph Application: Keeping Connections and Data Separate](#graph-application-keeping-connections-and-data-separate)
6. [BFS — Breadth First Search](#bfs--breadth-first-search)
7. [DFS — Depth First Search](#dfs--depth-first-search)
8. [BFS vs DFS — Quick Comparison](#bfs-vs-dfs--quick-comparison)

---

## The Core Insight
> *"A tree is just a graph with one rule: no cycles, one parent per node. Remove that rule and you get a graph — nodes can connect to anything."*

You have understood the mechanism perfectly. Yes, the values inside the array are indeed the keys of other nodes.

Here is exactly how those multiple keys fit into a single array, and why this design is a cornerstone of computer science.

---

## How Multiple Keys are Stored in an Array
In a dictionary, the value associated with a key does not have to be a single item; it can be a container data structure like an array (or a list in Python).

An array is a contiguous block of memory slots. Instead of storing data directly, each slot in that array stores a reference pointer to another key.

```text
Key [1] ──> Points to Array Container ──> Slot 0: Contains reference to Key [5]
                                          Slot 1: Contains reference to Key [6] 
```

When you define `1: [5, 6]`, Python allocates an array with two slots.
- Slot 0 holds the index/key for node 5.
- Slot 1 holds the index/key for node 6.

Because it is an array, you can add as many keys as you want (`[5, 6, 7, 8...]`), allowing a single node to branch out to dozens of different destinations.

---

## Why We Need This in Programming
We need this specific setup (a dictionary mapping keys to arrays of keys) because real-world data is highly interconnected, non-linear, and dynamic.

1. **Real-World Branching (One-to-Many Relationships)**
If a node could only point to a single value, your data could only form a straight line (like a simple chain). But the real world branches out.
On YouTube, one video (Key) has a list of 20 recommended videos (`[VideoB, VideoC, VideoD]`) in its array.
In a flight network, an airport like London Heathrow (Key) flies to hundreds of other cities simultaneously stored in its array.

2. **Speed and Efficiency (The Core Reason)**
If you did not use this structure, finding connections would be painfully slow.
*Without this structure:* To find out if Node 1 connects to Node 6, a computer would have to search through a massive, unorganized list of every single connection in the entire system line-by-line.
*With this structure:* The computer instantly jumps to Key 1 (takes less than a microsecond) and instantly reads its small array `[5, 6]`. It completely skips looking at nodes 0, 2, 3, 4, or 7.

3. **Handling Change Dynamically**
In programming, networks change constantly. If a user unfollows someone on social media, or a road closes on Google Maps, the computer does not have to rebuild the entire database. It simply looks up that specific Key and removes one number from its array.

---

## Graph Structure in Python

A graph is stored as a dictionary — each node maps to a list of its neighbours.

```python
graph = {
    "Alice":   ["Bob", "Charlie"],
    "Bob":     ["Alice", "Diana"],
    "Charlie": ["Alice", "Diana", "Eve"],
    "Diana":   ["Bob", "Charlie"],
    "Eve":     ["Charlie"]
}
```

---

## Graph Application: Keeping Connections and Data Separate (Recommended)
In big applications, programmers usually prefer to keep the graph structure (the map) completely separate from the actual data database. This keeps things incredibly clean.

You create two separate dictionaries:

**1. The Data Dictionary (The Encyclopedia)**
This only stores what the keys actually mean.
```python
node_data = {
    1: {"name": "Alice", "email": "alice@email.com"},
    2: {"name": "Bob", "email": "bob@email.com"},
    3: {"name": "Charlie", "email": "charlie@email.com"}
}
```

**2. The Graph Dictionary (The Map)**
This only stores how the numbers link together.
```python
graph = {
    1: [2, 3],
    2: [1],
    3: []
}
```

**How Python uses both together:**
If you are sitting at Node 1 and look at its graph array `[2, 3]`, you use those numbers to instantly pull the profile details from the `node_data` dictionary:

```python
current_node = 1
# Look up the neighbors in the graph map
for neighbor_key in graph[current_node]:
    # Look up the neighbor's actual data in the data dictionary
    neighbor_info = node_data[neighbor_key]
    print(f"Node {current_node} is connected to {neighbor_info['name']}")
```

**Output:**
```text
Node 1 is connected to Bob
Node 1 is connected to Charlie
```

---

## BFS — Breadth First Search

Uses a **queue**. Explores layer by layer — all nodes at distance 1 before distance 2.

**Guarantees the shortest path.**

> *"Go through direct friends first, then get information from them — check their friends. Layer by layer, closest first."*

### How the Friends Are Connected

```
         ┌─────────────────────────────────┐
         │                                 │
       Alice ──────── Charlie ──────── Eve
         │               │
        Bob ─────── Diana
```

More precisely — every edge in the graph:

```
  Alice ◄──────────────────────► Bob
    │                              │
    │                              │
    ▼                              ▼
 Charlie ◄───────────────────► Diana
    │
    │
    ▼
   Eve
```

### BFS traversal from Alice — step by step

```
Start:  Queue = [Alice]        Visited = {Alice}

Step 1: Pop Alice  → neighbours: Bob, Charlie
        Queue = [Bob, Charlie]  Visited = {Alice, Bob, Charlie}

Step 2: Pop Bob    → neighbours: Alice✗, Diana
        Queue = [Charlie, Diana]  Visited = {Alice, Bob, Charlie, Diana}

Step 3: Pop Charlie → neighbours: Alice✗, Diana✗, Eve
        Queue = [Diana, Eve]  Visited = {Alice, Bob, Charlie, Diana, Eve}

Step 4: Pop Diana  → neighbours: Bob✗, Charlie✗
        Queue = [Eve]

Step 5: Pop Eve    → TARGET FOUND  ✅  Steps = 2

Layer 0:  Alice
Layer 1:  Bob, Charlie       ← distance 1 from Alice
Layer 2:  Diana, Eve         ← distance 2 from Alice
```

> *"✗ means already visited — skip it. This is why the `visited` set is critical."*

### BFS Code

```python
from collections import deque

def bfs(graph, start, target):
    queue = deque()
    visited = set()

    queue.append((start, 0))    # (node, steps)
    visited.add(start)

    while queue:
        node, steps = queue.popleft()

        if node == target:
            return node, steps

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, steps + 1))

    return -1

print(bfs(graph, "Alice", "Eve"))      # ('Eve', 2)
print(bfs(graph, "Alice", "Diana"))    # ('Diana', 2)
print(bfs(graph, "Alice", "Alice"))    # ('Alice', 0)
```

**Why visited is a set:** Instant O(1) lookup prevents infinite loops. Without it, Alice → Bob → Alice → Bob → forever.

---

## DFS — Depth First Search

Uses a **stack**. Dives deep first — explores one full path before trying another.

**Finds a path — not necessarily the shortest.**

> *"DFS is like exploring a maze by always turning left — you'll eventually find the exit but maybe not the fastest way out."*

### DFS Code

```python
def dfs(graph, start, target):
    stack = []
    visited = set()

    stack.append((start, 0))
    visited.add(start)

    while stack:
        node, steps = stack.pop()     # pop() not popleft()

        if node == target:
            return node, steps

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append((neighbour, steps + 1))

    return -1
```

---

## BFS vs DFS — Quick Comparison

| | BFS | DFS |
|---|---|---|
| Data structure | Queue (`popleft`) | Stack (`pop`) |
| Explores | Layer by layer | Deep first |
| Shortest path | ✅ Guaranteed | ❌ Not guaranteed |
| Use for | Shortest path | Finding any path, all paths |

> *"popleft() mimics FIFO — first in first out. pop() mimics LIFO — last in first out. That one change completely flips how the graph is explored."*

---

*Extracted from Python DSA Mastery Notes — personal learning journal*
To understand Dijkstra's Algorithm, think of it as an upgraded version of BFS. Standard BFS assumes every connection (edge) takes exactly 1 step or 1 minute. But in the real world, roads have speed limits and traffic. Some roads take longer to travel than others. Dijkstra’s Algorithm adds a weight (cost, time, or distance) to each arrow to find the absolute fastest path, even if it means taking more steps.

### Step 1: The Problem with Standard BFS
Imagine you want to travel from Alice to Diana in this new network with road travel times (weights):

```text
       [5 mins]
 Alice ────────> Bob
   │               │
   │ [1 min]       │ [10 mins]
   ▼               ▼
Charlie ───────> Diana
        [2 mins]
```

- **If you use BFS:** It counts steps. It sees Alice -> Bob -> Diana is only 2 steps. It takes that path. Total time = \(5 + 10 = \mathbf{15\text{ minutes}}\).
- **If you use Dijkstra:** It counts actual time. It sees Alice -> Charlie -> Diana is 3 steps, but total time = \(1 + 2 = \mathbf{3\text{ minutes}}\). Dijkstra chooses this path because 3 < 15.

### Step 2: How Dijkstra's Code is Represented in Python
To make this work, our dictionary changes slightly. Instead of just a list of names, our array holds pairs of `(neighbor, weight)`.

```python
# Graph dictionary with weights (travel times)
weighted_graph = {
    "Alice": [("Bob", 5), ("Charlie", 1)],
    "Bob": [("Diana", 10)],
    "Charlie": [("Diana", 2)],
    "Diana": []
}
```

### Step 3: The Python Code Implementation
Instead of a standard queue (`popleft()`), Dijkstra uses a Priority Queue (via Python's `heapq` module). This special queue automatically sorts itself so that the node with the lowest total time is always processed first.

```python
import heapq

def dijkstra(graph, start, target):
    # Priority Queue stores pairs of: (total_time_so_far, current_node)
    # It automatically keeps the smallest total_time at the front!
    pq = [(0, start)]
    
    # Track the absolute shortest time discovered for each person
    shortest_times = {start: 0}

    while pq:
        # Pull the node that is currently quickest to reach
        current_time, current_node = heapq.heappop(pq)

        # If we reached our target, we are guaranteed to have the fastest path
        if current_node == target:
            return current_time

        # Look up the neighbors and their road travel times in the dictionary
        for neighbor, weight in graph[current_node]:
            time_to_neighbor = current_time + weight

            # If this new path is faster than any path we found before, save it!
            if neighbor not in shortest_times or time_to_neighbor < shortest_times[neighbor]:
                shortest_times[neighbor] = time_to_neighbor
                heapq.heappush(pq, (time_to_neighbor, neighbor))

    return float("inf") # Target unreachable

# Run the algorithm
fastest_time = dijkstra(weighted_graph, "Alice", "Diana")
print(f"The fastest travel time from Alice to Diana is: {fastest_time} minutes")
# Output: The fastest travel time from Alice to Diana is: 3 minutes
```

### Summary of the Graph Evolution
You have now moved through the three major stages of graph structures in programming:
- **Adjacency List:** Connecting keys to plain lists (`"Alice": ["Bob"]`).
- **BFS/DFS:** Using queues or stacks to step through those lists to count steps or explore paths.
- **Dijkstra:** Adding weights to the lists (`"Alice": [("Bob", 5)]`) and using a sorted priority queue to find the absolute most efficient path.
# 🐍 Python DSA Mastery Notes
> Personal learning journal — concepts, code, checkpoints, and understanding

---

## Table of Contents
1. [Week 1 — Data Structures](#week-1--data-structures)
   - [Lists](#lists)
   - [Dictionaries](#dictionaries)
   - [Sets](#sets)
   - [Tuples](#tuples)
   - [Stack](#stack)
   - [Queue](#queue)
   - [Project: URL Shortener](#project-url-shortener)
2. [Week 2 — Two Pointers & Sliding Window](#week-2--two-pointers--sliding-window)
   - [Two Pointers](#two-pointers)
   - [Sliding Window](#sliding-window)
   - [Project: Log File Analyzer](#project-log-file-analyzer)
3. [Week 3 — Recursion & Trees](#week-3--recursion--trees)
   - [Recursion](#recursion)
   - [Fibonacci + Memoization](#fibonacci--memoization)
   - [Binary Trees](#binary-trees)
4. [Week 4 — Binary Search, Sorting & Trie](#week-4--binary-search-sorting--trie)
   - [Binary Search](#binary-search)
   - [Merge Sort](#merge-sort)
   - [Trie — Autocomplete](#trie--autocomplete)
5. [Week 5 — Graphs, BFS & DFS](#week-5--graphs-bfs--dfs)
   - [BFS — Breadth First Search](#bfs--breadth-first-search)
   - [DFS — Depth First Search](#dfs--depth-first-search)
6. [Week 6 — Dynamic Programming](#week-6--dynamic-programming)
   - [Climb Stairs](#climb-stairs)
   - [Coin Change](#coin-change)
7. [Week 7 — Knapsack Problem](#week-7--knapsack-problem)

---

## Week 1 — Data Structures

### The Core Insight
> *"A dict doesn't search for the key — it calculates where the key lives. That's why it's instant regardless of size."*

---

### Lists

An ordered collection of items. Access by index. Slow to search — scans one by one.

```python
nums = [1, 2, 3, 4, 5]

# Accessing
nums[0]     # 1  — first item
nums[-1]    # 5  — last item
nums[2]     # 3  — middle item

# Adding
nums.append(6)       # adds to the END
nums.insert(0, 99)   # adds at index 0

# Removing
nums.pop()           # removes last item
nums.pop(0)          # removes at index 0
nums.remove(3)       # removes the value 3

# Looping
for num in nums:
    print(num)

for i, num in enumerate(nums):   # gives index AND value
    print(i, num)

# Checking
if 3 in nums:        # O(n) — scans the whole list
    print("found")
```

**When to use:** When you need order and duplicates.

---

### Dictionaries

Key-value pairs. Instant lookup — O(1). The most used data structure in real code.

> *"Each key in a dictionary is stored as a hash function — Python runs the key through a math formula that points to exactly where in memory the value lives."*

```python
person = {"name": "Shyjo", "age": 22, "place": "Kochi"}

# Adding / Updating
person["place"] = "Kollam"    # update existing key

# Reading
person["name"]                         # returns value — crashes if missing
person.get("name")                     # returns None if missing — safe
person.get("name", "unknown")          # returns "unknown" if missing

# Checking
if "name" in person:    # O(1) — instant

# Removing
del person["name"]
person.pop("name")

# Looping
for key, value in person.items():
    print(key, value)
```

**⚠️ Never name a variable `dict` — it overwrites Python's built-in.**

**When to use:** When you need to pair a key with a value.

#### Exercise — Count Frequency

```python
list1 = [3, 1, 4, 1, 5, 9, 2, 6]
counts = {}

for num in list1:
    if num in counts:
        counts[num] += 1    # seen before — add 1
    else:
        counts[num] = 1     # first time — start at 1

print(counts)
# {3:1, 1:2, 4:1, 5:1, 9:1, 2:1, 6:1}
```

> *"Use a dict to count — never use `.count()` inside a loop. That scans the whole list every time — O(n²)."*

---

### Sets

Like a list but no duplicates and instant lookup. Use when you only care if something EXISTS.

```python
s = {1, 2, 3, 3, 3}
print(s)    # {1, 2, 3} — duplicates removed automatically

# Adding
s.add(4)

# Checking — O(1) instant
if 3 in s:
    print("found")

# Removing duplicates from a list
nums = [1, 1, 2, 3, 3]
unique = set(nums)    # {1, 2, 3}

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b    # {3, 4}        — in BOTH
a | b    # {1,2,3,4,5,6} — in EITHER
a - b    # {1, 2}        — in a but NOT in b
```

#### Exercise — Detect Duplicate

```python
st = [1, 2, 3, 2, 1, 5]
seen = set()

for num in st:
    if num in seen:      # already saw this → duplicate
        print(True)
        break
    seen.add(num)
else:
    print(False)
```

> *"Whenever a problem says 'find duplicates' — reach for a set, not `.count()`."*

**When to use:** When you just need to know if something exists.

---

### Tuples

Like a list that can never be changed. Parentheses instead of brackets.

```python
point = (10, 20)
point[0]         # 10 — reading works
point[0] = 99    # ❌ ERROR — tuples are immutable

# Returning multiple values from a function
def get_user():
    return "Shyjo", 22       # Python returns this as a tuple

name, age = get_user()       # unpacking — use this constantly

# As dictionary keys — lists can't be dict keys
grid = {}
grid[(0, 0)] = "start"      # ✅ tuple as key
grid[[0, 0]] = "start"      # ❌ list as key — crashes
```

**When to use:** Fixed data that should never change, multiple return values, dict keys.

---

### Stack

Built using a list. **Last In, First Out — LIFO.**

> *"A stack is like a pile of plates. You put on top, you take from top. Last plate in, first plate out."*

**Real world uses:** Undo button, browser back button, Python call stack.

```python
stack = []

# Push — add to top
stack.append(1)
stack.append(2)
stack.append(3)
# stack = [1, 2, 3] — 3 is on top

# Pop — remove from top
stack.pop()     # returns 3
stack.pop()     # returns 2

# Peek — see top without removing
stack[-1]

# Check if empty
if not stack:
    print("empty")
```

#### Exercise — Valid Parentheses

```python
def is_valid(s):
    stack = []
    for i in s:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (i == ")" and top != "(") or \
               (i == "}" and top != "{") or \
               (i == "]" and top != "["):
                return False
    return len(stack) == 0

print(is_valid("({[]})"))   # True
print(is_valid("({)}"))     # False
```

**When to use:** When the ORDER of processing matters — last thing added needs to be handled first.

---

### Queue

Built using deque. **First In, First Out — FIFO.**

> *"A queue is like a coffee shop line. First person in, first person served."*

**Real world uses:** WhatsApp message delivery, print jobs, CPU scheduling.

```python
from collections import deque

queue = deque()

# Enqueue — add to back
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

# Dequeue — remove from front
queue.popleft()    # removes Alice — she's first

# ⚠️ KEY DIFFERENCE:
# Stack uses pop()      — removes from END   (LIFO)
# Queue uses popleft()  — removes from FRONT (FIFO)
```

#### Exercise — Hot Potato Game

```python
from collections import deque

def hot_potato(names, num):
    queue = deque(names)
    while len(queue) > 1:
        for i in range(num):
            queue.append(queue.popleft())   # pass potato
        eliminated = queue.popleft()        # person holding it is out
        print(f"{eliminated} eliminated")
    return queue[0]

print(hot_potato(["bob", "alice", "charlie", "david"], 2))
```

| | Stack | Queue |
|---|---|---|
| Rule | Last In First Out | First In First Out |
| Add | `append()` | `append()` |
| Remove | `pop()` — from end | `popleft()` — from front |
| Real world | Undo button | Printer queue |
| Built with | list | deque |

---

### Project: URL Shortener

> *"The same core logic that powers bit.ly — a dict, a hash function, file persistence. That's it."*

```python
import random
import string
import json

url_store = {}

def generate_code():
    characters = string.ascii_letters + string.digits
    code = ""
    for i in range(6):
        code += random.choice(characters)
    return code

def shorten_url(url):
    code = generate_code()
    url_store[code] = url
    return code

def retrieve_url(code):
    return url_store.get(code, "URL not found")

def save_data():
    with open("short_urls.json", "w") as file:
        json.dump(url_store, file)

def load_data():
    try:
        with open("short_urls.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Correct order — always
url_store = load_data()      # 1. load first
code = shorten_url("https://youtube.com")  # 2. shorten
save_data()                  # 3. save after
print(retrieve_url(code))
```

**Key lesson:** Load → Shorten → Save. Order matters.

---

## Week 2 — Two Pointers & Sliding Window

### The Core Insight
> *"Two pointers exploit sorted order to skip work. With an unsorted list there's no rule to guide which pointer to move — you'd be blind."*

---

### Two Pointers

Place one pointer at the start, one at the end. Move inward based on the result.

**Only works on sorted data** — sorted order gives you the decision rule.

```
[1, 2, 4, 6, 8]  target = 9
 ↑              ↑
left           right

sum = 1+8 = 9 → found!
sum too big  → move right inward
sum too small → move left inward
```

#### Two Sum — Sorted

```python
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1       # too small — need bigger number
        else:
            right -= 1      # too big — need smaller number

    return None

print(two_sum_sorted([1, 3, 5, 7, 9], 10))   # [0, 4]
print(two_sum_sorted([1, 3, 5, 7, 9], 8))    # [1, 2]
```

#### Palindrome Check

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
```

---

### Sliding Window

Both pointers start at the left and move right together. Maintains a window of elements between them.

> *"Like a magnifying glass sliding across the list. The window can grow or shrink as you move."*

**Works on any data** — both pointers move in the same direction.

#### Max Window Sum

```python
def max_window_sum(nums, k):
    if k > len(nums):
        return None

    window_sum = sum(nums[:k])    # calculate first window
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]   # add new, drop old
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))   # 9
```

> *"The key line: `window_sum += nums[i] - nums[i-k]`. Add the new number coming in, subtract the old number leaving. Never recalculate the whole window."*

| | Two Pointers | Sliding Window |
|---|---|---|
| Direction | One each end, move inward | Both move same direction |
| Needs sorted | Yes | No |
| Use for | Pairs, palindromes | Subarrays, substrings |

---

### Project: Log File Analyzer

```python
from collections import deque

timestamps = [1, 15, 45, 79, 110, 120, 150, 180, 210, 240, 270, 300]

def find_busiest_window(timestamps, window_size=60):
    window = deque()
    max_requests = 0

    for timestamp in timestamps:
        window.append(timestamp)

        # remove timestamps outside the 60s window
        while window and window[0] <= timestamp - window_size:
            window.popleft()

        max_requests = max(max_requests, len(window))

    return max_requests

print(f"Busiest window: {find_busiest_window(timestamps)} requests")
```

**Key lesson:** Every timestamp enters the deque once and leaves once — total 2n operations. That's why it's O(n) not O(n²) even with a while loop inside a for loop.

---

## Week 3 — Recursion & Trees

### The Core Insight
> *"Recursion works when a problem has this shape: 'This big problem is just a small version of itself, repeated.'"*

---

### Recursion

Every recursive function has exactly two parts:

**Base case** — the stopping condition. The simplest version that needs no further breaking down.

**Recursive case** — the function calls itself on a smaller version of the problem.

```python
# The Two Rules of Recursion:
# 1. Always have a base case
# 2. Every recursive call must move toward the base case
```

#### Folder Counter

```python
folder = {
    "files": ["notes.txt", "photo.jpg"],
    "subfolders": [
        {
            "files": ["report.pdf"],
            "subfolders": []
        },
        {
            "files": ["music.mp3", "video.mp4"],
            "subfolders": [
                {
                    "files": ["data.csv"],
                    "subfolders": []
                }
            ]
        }
    ]
}

def count_files(folder):
    # Base case — no subfolders
    if not folder["subfolders"]:
        return len(folder["files"])

    # Recursive case — count files here + all subfolders
    total_files = len(folder["files"])
    for subfolder in folder["subfolders"]:
        total_files += count_files(subfolder)

    return total_files

print(count_files(folder))   # 6
```

---

### Fibonacci + Memoization

```python
# Naive recursion — O(2ⁿ) — exponentially slow
def fib_slow(n):
    if n == 1 or n == 2:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)

# With memoization — O(n) — each value calculated once
def fib(n, memo={}):
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]           # already solved — return instantly
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))    # 55
print(fib(50))    # 12586269025 — instant
```

> *"Memoization uses a dictionary to store results. Dict lookup is O(1) — so checking 'have I calculated this before?' is instant. That's why it's the right data structure."*

**fib(50) without memo:** 2²⁵ = 33 million recursive calls.
**fib(50) with memo:** 49 calls. Same answer. 99.999% less work.

---

### Binary Trees

A tree where each node has a value and up to two children — left and right.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Build a tree
#        10
#       /  \
#      5    15
#     / \     \
#    3   7    20

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)

# Pre-order traversal — print before recursing
def print_tree(node):
    if node is None:          # base case — empty node, stop
        return
    print(node.value)         # print current
    print_tree(node.left)     # recurse left
    print_tree(node.right)    # recurse right

print_tree(root)   # 10 5 3 7 15 20
```

**Three traversal types:**
- **Pre-order** — print, left, right → `10 5 3 7 15 20`
- **In-order** — left, print, right → `3 5 7 10 15 20` (sorted!)
- **Post-order** — left, right, print → `3 7 5 20 15 10`

> *"Moving `print(node.value)` to after the two recursive calls gives post-order. Every node still gets printed — but only after its entire subtree is done. Deepest nodes print first, root prints last."*

---

## Week 4 — Binary Search, Sorting & Trie

### The Core Insight
> *"Binary search halves your search space every step. log(1,000,000) = 20 operations. The most elegant algorithm in computer science."*

---

### Binary Search

Works only on **sorted** data. Each step throws away half the remaining list.

> *"Start from the middle. If the number is high, take the right side and split half."*

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid           # found it
        elif target < nums[mid]:
            right = mid - 1      # too big — search left half
        else:
            left = mid + 1       # too small — search right half

    return -1    # not found

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))    # 3
print(binary_search(nums, 6))    # -1
```

**Time complexity:** O(log n) — 1,000,000 items → maximum 20 checks.

---

### Merge Sort

Divide and conquer. Split in half, sort each half, merge back together. O(n log n).

```python
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]     # add leftovers
    result += right[j:]
    return result

def merge_sort(nums):
    if len(nums) <= 1:     # base case — already sorted
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])    # sort left half
    right = merge_sort(nums[mid:])   # sort right half
    return merge(left, right)        # combine

nums = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(nums))   # [3, 9, 10, 27, 38, 43, 82]
```

**Combining both:**
> *"Sort once with merge sort — pay O(n log n) once. Then binary search many times at O(log n) each. That's how databases and search systems work."*

---

### Trie — Autocomplete

A tree where each node is a letter. Paths through the tree spell words. Search by prefix in O(word length) regardless of dictionary size.

> *"Think of it like folders on a computer: `{ 'c': { 'a': { 't': {} } } }` — nested dicts all the way down."*

```python
class TrieNode:
    def __init__(self):
        self.children = {}     # letter → next TrieNode
        self.is_end = False    # does a word end here?

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()   # create if missing
            node = node.children[char]              # move deeper
        node.is_end = True                          # mark word end

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        words = []
        self._collect_words(node, prefix, words)
        return words

    def _collect_words(self, node, prefix, words):
        if node.is_end:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, words)

trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("card")
trie.insert("care")
trie.insert("dog")

print(trie.search("ca"))    # ["cat", "car", "card", "care"]
```

**Why `is_end` matters:** Without it you can't tell if "car" is a complete word or just a prefix of "card". Every path would keep going with no stopping point.

---

## Week 5 — Graphs, BFS & DFS

### The Core Insight
> *"A tree is just a graph with one rule: no cycles, one parent per node. Remove that rule and you get a graph — nodes can connect to anything."*

You have understood the mechanism perfectly. Yes, the values inside the array are indeed the keys of other nodes.

Here is exactly how those multiple keys fit into a single array, and why this design is a cornerstone of computer science.

#### How Multiple Keys are Stored in an Array
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

#### Why We Need This in Programming
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

### Graph Structure in Python

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

#### Graph Application: Keeping Connections and Data Separate (Recommended)
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

### BFS — Breadth First Search

Uses a **queue**. Explores layer by layer — all nodes at distance 1 before distance 2.

**Guarantees the shortest path.**

> *"Go through direct friends first, then get information from them — check their friends. Layer by layer, closest first."*

#### How the Friends Are Connected

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

**BFS traversal from Alice — step by step:**

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

### DFS — Depth First Search

Uses a **stack**. Dives deep first — explores one full path before trying another.

**Finds a path — not necessarily the shortest.**

> *"DFS is like exploring a maze by always turning left — you'll eventually find the exit but maybe not the fastest way out."*

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

| | BFS | DFS |
|---|---|---|
| Data structure | Queue (popleft) | Stack (pop) |
| Explores | Layer by layer | Deep first |
| Shortest path | ✅ Guaranteed | ❌ Not guaranteed |
| Use for | Shortest path | Finding any path, all paths |

> *"popleft() mimics FIFO — first in first out. pop() mimics LIFO — last in first out. That one change completely flips how the graph is explored."*

---

## Week 6 — Dynamic Programming

### The Core Insight
> *"DP is just: break a big problem into smaller subproblems, solve each subproblem once, store the result, never solve it again."*

**Two approaches:**
- **Memoization (top-down)** — start with big problem, recurse down, cache results
- **Tabulation (bottom-up)** — start with smallest subproblems, fill a table upward

---

### Climb Stairs

You can climb 1 or 2 steps at a time. How many ways to reach step n?

```
Ways for staircase:
1 step  → 1 way
2 steps → 2 ways
3 steps → 3 ways
4 steps → 5 ways   ← Fibonacci pattern!

ways(n) = ways(n-1) + ways(n-2)
```

```python
def climb_stairs(n):
    if n == 1:
        return 1
    table = [0] * (n + 1)
    table[1] = 1    # base case — set manually
    table[2] = 2    # base case — set manually
    for i in range(3, n + 1):
        table[i] = table[i-1] + table[i-2]   # fill the table
    return table[n]

print(climb_stairs(4))    # 5
print(climb_stairs(10))   # 89
```

> *"We start filling the table from index 3 because we already set table[1] and table[2] manually — no need to recalculate what we already know."*

---

### Coin Change

Given coins and an amount, find the minimum number of coins to make that amount.

```python
def min_coins(coins, amount):
    table = [float('inf')] * (amount + 1)   # start as impossible
    table[0] = 0                             # base case: 0 coins for 0 amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # i-coin checks the balance — add 1 for the current coin
                table[i] = min(table[i], table[i - coin] + 1)

    return table[amount] if table[amount] != float('inf') else -1

print(min_coins([1, 5, 10], 11))    # 2 → 10+1
print(min_coins([1, 5, 10], 36))    # 5
print(min_coins([2], 3))            # -1 → impossible
```

**Why `float('inf')`:** Infinity signals "not yet possible." Using 0 would confuse "needs 0 coins" with "hasn't been solved yet."

**Why `[2], 3` returns -1:** Coin 2 can only make even numbers. 3 is odd. No combination of 2s ever reaches 3. table[3] stays infinity.

> *"`table[i - coin] + 1` — check the balance of the amount and find how many coins used. If it's infinity, infinity plus one is still infinity. If it's not, add one more for the coin just used."*

---

## Week 7 — Knapsack Problem

### The Core Insight
> *"Any problem asking 'maximize value given a constraint' is knapsack."*

**The problem:** You have a bag with weight capacity. Items have weights and values. Maximize total value without exceeding capacity.

```
Item     Weight   Value
─────────────────────────
Laptop     3kg    £4000
Phone      1kg    £1000
Camera     4kg    £3000
Tablet     5kg    £2000
Capacity:  10kg
```

### 2D DP Table

Each cell answers: *"what is the maximum value using the first i items with capacity j?"*

For each item at each capacity, ask two questions:
- **Leave it** → same value as without this item
- **Take it** → this item's value + best value with remaining capacity

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            leave = table[i-1][j]                              # leave the item

            if weights[i-1] <= j:                              # item fits
                take = values[i-1] + table[i-1][j - weights[i-1]]
                table[i][j] = max(leave, take)                 # take the best
            else:
                table[i][j] = leave                            # can't fit — leave

    return table[n][capacity]

weights  = [3, 1, 4, 5]
values   = [4000, 1000, 3000, 2000]
capacity = 10

print(knapsack(weights, values, capacity))   # 8000
```

**Base cases:**
- `table[i][0] = 0` — capacity 0, carry nothing
- `table[0][j] = 0` — no items, value is 0

---

## Key Decision Guide — When to Use What

| Data Structure | Use When |
|---|---|
| List | You need order and duplicates |
| Dictionary | You need to pair a key with a value |
| Set | You just need to know if something exists |
| Tuple | Data is fixed and should never change |
| Stack | Last thing in must be handled first (undo, brackets) |
| Queue | First thing in must be handled first (scheduling, BFS) |

| Algorithm | Use When |
|---|---|
| Two Pointers | Sorted data, finding pairs, palindromes |
| Sliding Window | Subarrays, substrings, time windows |
| BFS | Shortest path in a graph |
| DFS | Finding any path, exploring all options |
| Binary Search | Finding in sorted data — O(log n) |
| Merge Sort | Sorting general data — O(n log n) |
| Memoization | Top-down DP, recursive problems |
| Tabulation | Bottom-up DP, optimization problems |

---

## The Questions That Make You Think Like an Engineer

Before writing any code, ask yourself:

1. **"Can a dict or set answer this instead of a loop?"** → O(1) vs O(n)
2. **"Am I doing extra work inside this loop?"** → avoid `.count()` inside loops
3. **"Is the data sorted? Can I use binary search or two pointers?"**
4. **"Am I solving the same subproblem twice?"** → use memoization
5. **"Do I need the shortest path?"** → BFS, not DFS
6. **"Is this problem just a smaller version of itself?"** → use recursion

---

*Generated from personal learning sessions — Python DSA Mastery Curriculum*

Everything is now 100% Python. Here's what changed across all 20 weeks:
Projects are now real Python things you'd actually build:

URL Shortener CLI → pure Python dict + json
Log Analyzer → file I/O + sliding window
Task Queue → heapq + dataclasses
Browser History → doubly linked list OOP
File System Tree → pathlib + recursion
Git Diff Clone → LCS algorithm + colorama
City Route Finder → Dijkstra + heapq
Capstone → FastAPI + SQLite + everything


Week 1: Arrays & Dictionaries — The Core Idea
Start with this question: how do you find something?
Imagine I give you a list of 1000 names written on paper and ask "is Sarah in this list?" What do you do? You scan from the top. One by one. That's what a computer does with a list — it checks every single item until it finds what you need. If Sarah is last, you waited through 999 names for nothing. This is called O(n) — the time it takes grows with the size of the list.
Now imagine instead I give you a phone book. You don't scan from page 1. You flip directly to "S" and land near Sarah instantly. That's a dictionary — also called a hashmap. Under the hood, Python takes your key, runs it through a math formula called a hash function, and that formula tells it exactly where in memory to look. No scanning. No waiting. Just — jump. This is O(1) — constant time, instant, regardless of size.

The Three Things to Burn Into Your Brain:
One — A Python list is ordered but slow to search. You find things by scanning.
Two — A Python dict is a key-value store. You find things by asking. The asking is instant.
Three — Whenever you catch yourself writing a loop just to find something — stop. Ask yourself: could a dict answer this question instead?

- I use dict as object name should avoid that 

# Exercise 3 

Given a list [3, 1, 4, 1, 5, 9, 2, 6], loop through it and count how many times each number appears using a dict. At the end, print the dict.
That last exercise is the foundation of 30% of all LeetCode problems.

count= {}
list1=[3, 1, 4, 1, 5, 9, 2, 6]
for i int list1:
    dic1[i] = list1.count(i)
print(dic1)
Your solution works but it has a hidden inefficiency. list1.count(i) scans the entire list every single time through the loop. So if the list has 8 items, you're scanning 8 times × 8 items = 64 operations. For a million items that becomes a serious problem.
list1 = [3, 1, 4, 1, 5, 9, 2, 6]
counts = {}

for num in list1:
    if num in counts:
        counts[num] += 1    # seen before — add 1
    else:
        counts[num] = 1     # first time seeing it — start at 1

print(counts)

The Python Data Structures Map
Think of it as a ladder. You've climbed the first two rungs.
Rung 1 — List ✅ You know this. Ordered collection. Access by index. Slow to search.
Rung 2 — Dictionary ✅ You know this. Key-value pairs. Instant lookup. The powerhouse.
Rung 3 — Set ← next. Like a list but no duplicates and instant lookup. Simpler than a dict when you only care if something EXISTS, not what it maps to.
Rung 4 — Tuple ← quick one. Like a list that can never be changed. Used for fixed data.
Rung 5 — Stack ← built using a list. Last in, first out. Think undo button.
Rung 6 — Queue ← built using deque. First in, first out. Think a line of people waiting.

Let's Do Set Right Now
You already understand dict. A set is just a dict where you only care about the keys — no values.
pythonseen = set()         # empty set
seen = {1, 2, 3}     # set with items — notice NO key:value pairs
Three things it does that make it powerful:
One — no duplicates ever
pythonnums = [1, 1, 2, 3, 3, 3]
unique = set(nums)
print(unique)   # {1, 2, 3} — duplicates gone
Two — instant lookup, just like dict
pythonif 3 in unique:    # O(1) — instant, not O(n) like a list
    print("found")
Three — set operations — this is the beautiful part
pythona = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b    # intersection → {3, 4}   what's in BOTH
a | b    # union → {1, 2, 3, 4, 5, 6}   everything
a - b    # difference → {1, 2}   in a but NOT in b

When to Use What — The Decision
This is the question senior developers ask instinctively. Train yourself to ask it every time:
"Do I need to store pairs of data?" → Dictionary
"Do I just need to remember if I've seen something?" → Set
"Do I need order and duplicates?" → List
"Is this data fixed and never changing?" → Tuple

Stack — Last In, First Out
Let me give you the real world picture first.
Think about a stack of plates. You put a plate on top. You put another on top of that. When you take a plate — you take from the top. You can't pull from the middle or the bottom. The last plate you put on is the first one you take off.
That's a stack. Last In, First Out. LIFO.

Where You Already Use Stacks Every Day
Undo button. Every time you type a letter in VS Code and hit Ctrl+Z, it undoes the last thing. The editor is pushing every action onto a stack. Undo pops the top one off.
Browser back button. Every page you visit gets pushed onto a stack. Hit back — it pops the top page off and takes you to the one beneath it.
Python's own call stack. When a function calls another function, Python pushes it onto a stack. When it finishes, it pops off and returns to where it was. When you see an error traceback in Python, that's the call stack printed out.

How You Build It in Python
Python doesn't have a built-in "Stack" type. You build one using a list. Only two operations matter:
Push — add something to the top
pythonstack = []
stack.append(1)    # push 1
stack.append(2)    # push 2
stack.append(3)    # push 3
# stack is now [1, 2, 3] — 3 is on top
Pop — remove from the top
pythonstack.pop()    # removes 3 → returns 3
stack.pop()    # removes 2 → returns 2
# stack is now [1]
That's it. A stack is just a list where you only ever touch the end.

The Golden Rule
A stack has only two questions it can answer:
"What's on top?"
pythonstack[-1]    # peek at top without removing
"Is it empty?"
pythonif not stack:
    print("empty")
You never access the middle. You never access the bottom. Only the top.


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

# 30% of all LeetCode problems.

- list1 = [3, 1, 4, 1, 5, 9, 2, 6]
- counts = {}

- for num in list1:
    if num in counts:
        counts[num] += 1    # seen before — add 1
    else:
        counts[num] = 1     # first time seeing it — start at 1

- print(counts)

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

Queue — First In, First Out
Let me give you the real world picture first.
Think about a queue of people waiting at a coffee shop. The first person who joined the line gets served first. The last person who joined waits the longest. Nobody cuts in from the middle. First In, First Out. FIFO.
That's the exact opposite of a stack.

Where You Already See Queues Every Day
WhatsApp messages. Messages are delivered in the order they were sent. First message sent, first message received. That's a queue.
Print jobs. Send three documents to a printer. They print in the order you sent them. Queue.
YouTube video loading. Buffering loads chunks of video in order — chunk 1, chunk 2, chunk 3. Queue.
CPU task scheduling. Your operating system uses queues to decide which program runs next.

Why Not Just Use a List?
You could. But there's a problem. Removing from the front of a list is slow — O(n) — because Python has to shift every remaining item one position to the left. Imagine doing that a million times.
Python gives us a better tool — deque (pronounced "deck"). It stands for double ended queue. It can add and remove from both ends in O(1) — instant.
pythonfrom collections import deque

queue = deque()
That one import is all you need.

The Two Operations
Enqueue — join the back of the line
pythonqueue.append("Alice")     # Alice joins
queue.append("Bob")       # Bob joins behind Alice
queue.append("Charlie")   # Charlie joins behind Bob
# queue → Alice, Bob, Charlie
# Alice is at the front, Charlie at the back
Dequeue — serve from the front of the line
pythonqueue.popleft()    # removes Alice → she gets served first
queue.popleft()    # removes Bob
# queue → Charlie
Notice — popleft() not pop(). That's the key difference from a stack. Stack uses pop() — takes from the end. Queue uses popleft() — takes from the front.

Stack vs Queue Side by Side
This is worth burning into your brain:
StackQueueRuleLast In First OutFirst In First OutAddappend()append()Removepop() — from endpopleft() — from frontReal worldUndo buttonPrinter queueBuilt withlistdeque

Your Exercise
Two exercises — same pattern as before:
Exercise 1 — Simulate a coffee shop queue. Three customers join: "Alice", "Bob", "Charlie". Serve them one by one using popleft(). Print who gets served each time.
Exercise 2 — Hot Potato game. Given a list of names and a number n, pass the "potato" around the queue n times. The person holding it after n passes gets eliminated. Keep going until one person is left — they win.
Walk through exercise 2 in plain English first before coding: every round you move the front person to the back n times, then the person at the front is out. Repeat until one remains.
Paste your code back when ready. Once this is done — you have all six data structures. We move straight into the first real algorithm pattern and start building your URL Shortener project.
from collections import deque

lis = ["bob", "alice", "charlie", "david"]
num = 2
que = deque(lis)

while len(que) > 1:
    for i in range(num):
        que.append(que.popleft())   # pass potato num times
    eliminated = que.popleft()      # ← THIS LINE — person holding it is out
    print(f"{eliminated} is eliminated")

print("Winner:", que[0])

One More Before the Project — Sliding Window
Before we build the Log File Analyzer, you need to feel the sliding window pattern. It's the other half of this week.
Here's the problem in plain English:
Given a list of numbers [2, 1, 5, 1, 3, 2] and a window size k = 3, find the maximum sum of any 3 consecutive numbers.
The brute force way — calculate the sum of every possible group of 3. That's O(n×k).
The sliding window way — calculate the first window's sum, then slide right by adding the new number and dropping the old one. Never recalculate the whole window. O(n).
[2, 1, 5, 1, 3, 2]   k=3

Window 1: 2+1+5 = 8
Slide →  drop 2, add 1 → 1+5+1 = 7
Slide →  drop 1, add 3 → 5+1+3 = 9  ← maximum
Slide →  drop 1, add 2 → 1+3+2 = 6
Write this function:
pythondef max_window_sum(nums, k):
    # calculate first window sum
    # slide across the rest
    # track the maximum
    # return it

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_window_sum([1, 4, 2, 9, 7, 3], 2))  # 16
Think before coding — how do you slide the window? You add nums[right] and drop nums[right - k]. That's the key insight. Write it and paste back.def max_window_sum(nums, k):
    if k > len(nums):
        return None
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
  
    # slide across the rest
    # track the maximum
    # return it

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_window_sum([1, 4, 2, 9, 7, 3], 2))  # 16Show lessMar 7Validated sliding window algorithm implementation thoroughlyValidated sliding window algorithm implementation thoroughlyThat is exceptional. Genuinely impressive code.

Every line is correct and professional:
pythonif k > len(nums):
    return None              # ✅ edge case handled — window bigger than list

window_sum = sum(nums[:k])   # ✅ first window calculated cleanly
max_sum = window_sum         # ✅ starts max at first window

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]   # ✅ slide — add new, drop old
    max_sum = max(max_sum, window_sum)     # ✅ track maximum

return max_sum               # ✅ clean return

The line that shows you truly understood it:
pythonwindow_sum += nums[i] - nums[i - k]
You didn't recalculate the whole window. You added the new number coming in and subtracted the old number leaving. That's the entire sliding window insight in one line. Most beginners miss this and recalculate from scratch every time — O(n×k). Yours is O(n).

Week 2 Complete
Look what you've mastered this week:

Two Sum Sorted — two pointers from opposite ends ✅
Palindrome Check — two pointers comparing characters ✅
Max Window Sum — sliding window, add and drop ✅


Checkpoint — Answer These Before We Move On
Three questions, plain English, no code:
One — What's the difference between two pointers and sliding window?
Two — Why does two pointers only work on a sorted list for the two sum problem?
Three — In your sliding window solution, what does nums[i - k] represent?
Answer all three and we move straight into building the Log File Analyzer project — where you use sliding window on real data.in two pointers we need to know length of list and also need sorted list. two pointers on not sorted list makes it remove not smallest one from the k and finally num[i-k] is the position of the first number in the window

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

dict[i]= {}
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

Dictionary access is by key, not by position.
It is not like a list index.
Example:
If counts is {3: 1, 1: 2}, then:

counts[3] is 1
counts[1] is 2
counts[0] gives error unless key 0 exists

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

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Method 1: using &
intersection_result = a & b
print(intersection_result)   # {3, 4}

# Method 2: using intersection()
intersection_result2 = a.intersection(b)
print(intersection_result2)  # {3, 4}

# Tuple
This one is quick, five minutes max. A tuple is just a list that cannot be changed after you create it.
pythonpoint = (10, 20)       # parentheses instead of brackets
point[0]               # 10 — reading works fine
point[0] = 99          # ❌ ERROR — tuples don't allow this

tuple usage 
-> coordinate and fixed pairs of data that should never change 
-> returning multiple values from a function 
def get_user():
    return "Shyjo", 22       # Python returns this as a tuple

name, age = get_user()       # unpacking — you'll use this constantly
-> tuple as a dictionary key is valid 
grid = {}
grid[(0, 0)] = "start"     # tuple as a key — valid
grid[(1, 2)] = "player"


# When to Use What — The Decision This is the question senior developers ask instinctively. Train yourself to ask it every time:
"Do I need to store pairs of data?" → Dictionary
"Do I just need to remember if I've seen something?" → Set
"Do I need order and duplicates?" → List
"I"s this data fixed and never changing?" → Tuple
--list -- dict --- set --- tuple --

# Stack — Last In, First Out
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

def is_valid(s):
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # If it's a closing bracket 
        if char in mapping: # here in mapping dictionary it looks for key
                            #if mapping.values() looks   for values 
            # Pop the top element if stack isn't empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the popped element doesn't match the mapping, it's invalid
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack
 Examples:
 print(is_valid("(())")) -> True
print(is_valid("({)}")) -> False


# Queue — First In, First Out
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

from collections import deque

queue = deque()


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
# url shortner 
"""
Simple URL Shortener (Beginner Version)

What this program does:
1. Loads old short codes from a JSON file.
2. Generates a random 6-character code.
3. Stores code -> original URL in a Python dictionary.
4. Saves updated dictionary back to JSON.
5. Retrieves the original URL using the short code.

Why JSON?
- JSON is used here as simple file storage.
- In real projects, this is usually stored in a database.
"""

a hash function — a math formula that converts the key into a number, and that number points to an exact location in memory. Python jumps directly there.
Think of it like this:
List — finding something is like searching a book page by page. More pages = more time. O(n).
Dict — finding something is like using the book's index. No matter how big the book, the index tells you exactly which page to go to. Instant. O(1).

# two pointer 
Where You'll Use This in Real Code

-Finding pairs in sorted data
-Checking if a string is a palindrome
-Removing duplicates from a sorted list
-Comparing two strings character by character
-Merging two sorted lists

palindrome
    # use two pointers
    # compare characters from both ends
    # if any pair doesn't match → return False
    # if pointers cross → return True


# sliding window - same idea different shape


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

# recursion and trees

A folder can contain files or other folders. Those folders can contain more files or folders, and so on forever. How would you write code to count every single file no matter how deep they're nested?

Try to think it through. Your folder structure looks like this:
Documents/
    Work/
        Projects/
            2024/
                report.pdf
            notes.txt
        budget.xlsx
    Personal/
        photos/
            holiday.jpg

How deep does it go? You don't know.
"To count all files in a folder — count the files directly inside it, then do the same thing for each subfolder inside it."

count_files(Documents)
    → count files in Documents directly
    → count_files(Work)          ← same function, smaller problem
        → count_files(Projects)  ← smaller again
            → count_files(2024)  ← smallest — just files, no folders
        → count files in Work
    → count_files(Personal)
        → count_files(photos)

Recursion works when a problem has this shape:
"This big problem is just a small version of itself, repeated."

The function stops calling itself when it reaches a folder that has no subfolders inside it — only files. There's nothing left to go deeper into. That's the stopping condition.
In recursion this is called the base case. Every recursive function has two parts:
Base case — the condition where the function stops calling itself. The simplest version of the problem that needs no further breaking down.
Recursive case — where the function calls itself on a smaller version of the problem.

The Folder Counter — In Plain English
def count_files(folder):

    BASE CASE:
    if folder has no subfolders:
        return number of files directly in it

    RECURSIVE CASE:
    total = files directly in this folder
    for each subfolder:
        total += count_files(subfolder)  ← calls itself
    return total

Your Exercise
Before we write real file system code, let's practice recursion on something simpler — a nested dictionary that represents a folder structure:
pythonfolder = {
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
Write a recursive function count_files(folder) that counts every file at every level.
The answer should be 7 — notes.txt, photo.jpg, report.pdf, music.mp3, video.mp4, data.csv = 6... count them yourself first to verify.
Two hints:
Hint 1 — base case is when subfolders is empty — just return len(folder["files"])
Hint 2 — recursive case adds len(folder["files"]) plus calls itself on each subfolder
Write it and paste back. This is the concept that unlocks trees, graphs, and everything in Week 

if not folder["subfolders"]:
    return len(folder["files"])      # ✅ base case — no subfolders, count files

total_files = len(folder["files"])   # ✅ count files at current level
for subfolder in folder["subfolders"]:
    total_files += count_files(subfolder)  # ✅ recursive case — trust the function
return total_files                   # ✅ return total
```

And the answer is 6 — notes.txt, photo.jpg, report.pdf, music.mp3, video.mp4, data.csv.

---

## What Just Happened in Your Code

When you called `count_files(folder)` Python built this call stack:
```
count_files(Documents)        → 2 files
  count_files(Work)           → 1 file
  count_files(Personal)       → 2 files
    count_files(nested)       → 1 file
                              = 6 total
```

Each call solved a smaller version of the same problem. Each one trusted the function below it to handle the rest. That's recursion working exactly as designed.

---

## The Two Rules of Recursion — Memorise These

**Rule 1 — Always have a base case.** The condition that stops the function calling itself. Without it you get infinite recursion and Python crashes.

**Rule 2 — Every recursive call must move toward the base case.** Each call works on something smaller than the previous one. Subfolders are always smaller than the parent folder.

---

## Now The Real Challenge — Fibonacci

This is the classic recursion problem every programmer learns. It also teaches you why recursion can be slow — and how to fix it.

The Fibonacci sequence: `1, 1, 2, 3, 5, 8, 13, 21...`

Each number is the sum of the two before it.
```
fib(1) = 1
fib(2) = 1
fib(3) = fib(2) + fib(1) = 2
fib(4) = fib(3) + fib(2) = 3
fib(5) = fib(4) + fib(3) = 5

What is the base case?
fib(1) = 1
fib(2) = 1
What is the recursive case?

def fib(n):
    # base case 1
    if n == 1:
        return 1
    # base case 2
    if n == 2:
        return 1
    # recursive case — just two calls added together
    return fib(n-1) + fib(n-2)

# memoization

if the problem need ot solve twice use memoization 
def fib(n, memo={}):
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]      # already calculated — return instantly
    memo[n] = fib(n-1, memo) + fib(n-2, memo)  # store it
    return memo[n]

# binary tree 

A binary tree is just a recursive structure — each node has a value and up to two children. Left and right. Those children are also nodes with their own left and right. It goes as deep as needed.

        10
       /  \
      5    15
     / \     \
    3   7    20

Build a Tree Node in Python
A tree node is just a simple class:
python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None    # left child
        self.right = None   # right child
Build the tree above manually:
pythonroot = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)



def print_tree(node):
    # base case — if node is None, stop
    if node is None:
        return

    # print current node's value
    print(node.value)

    # recurse into left child
    print_tree(node.left)

    # recurse into right child
    print_tree(node.right)

    print_tree(10)
    print 10
    print_tree(5)
        print 5
        print_tree(3)
            print 3
            print_tree(None) → return
            print_tree(None) → return
        print_tree(7)
            print 7
            print_tree(None) → return
            print_tree(None) → return
    print_tree(15)
        print_tree(None) → return
        print_tree(20)
            print 20
            print_tree(None) → return
            print_tree(None) → return

Output: 10 5 3 7 15 20

One — What is the base case for a tree traversal and why?
if node is None:
    return
Two — What happens if you move print(node.value) to after the two recursive calls instead of before?
so here the tree from  3 7 5 20 15 10 that prints form backward
Three — Your fibonacci used a dict for memoization. Your tree traversal didn't need one. Why not?
in fibonacci the nodes or points are visited once but in tree thats not the case the nodes are visited once

# Binary search 

Start at the middle ✅
Number too high → take the right half ✅
Number too low → take the left half ✅
Split and repeat ✅

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2    # middle index

    if target == nums[mid]:
        return mid                # ✅ found it — return index

    elif target < nums[mid]:
        right = mid - 1           # ✅ too big — throw away right half

    else:
        left = mid + 1            # ✅ too small — throw away left half

    return -1   # not found

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))    # 3
print(binary_search(nums, 1))    # 0
print(binary_search(nums, 15))   # 7
print(binary_search(nums, 6))    # -1 not found

# merge sort 

Look at the front of each list
Pick the smaller one
Append it to the result
Repeat until both lists are empty
def merge(left, right):
    result = []
    i = 0   # pointer for left list
    j = 0   # pointer for right list

    # while both lists have items
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:           
            result.append(right[j])
            j += 1
        # compare front of each list
        # append the smaller one
        # move that pointer forward

    # one list may have leftovers — add them
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(nums):
    # base case — list of 1 or 0 items is already sorted
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])    # sort left half
    right = merge_sort(nums[mid:])   # sort right half
    return merge(left, right)        # merge them back

nums = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(nums))   # [3, 9, 10, 27, 38, 43, 82]

[38, 27, 43, 3, 9, 82, 10]
        ↓ split
[38, 27, 43]     [3, 9, 82, 10]
    ↓ split           ↓ split.    spit then merge function 
[38] [27, 43]   [3, 9] [82, 10]
      ↓ merge     ↓ merge  ↓ merge
    [27, 38, 43] [3, 9] [10, 82]
              ↓ merge
        [3, 9, 10, 27, 38, 43, 82]

# tire node 

trie is a tree like data structure that stores a dynamic set of strings,

the dictionaries is used nad is_end is important if not the program dosent know the ending of the word

class TrieNode:
    def __init__(self):
        self.children = {}    # letter → next TrieNode every single node is a character and it has a dictionary of its children
        self.is_end = False   # does a word end here?

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # create if missing
            node = node.children[char]             # move deeper
        node.is_end = True                         # mark word end

    def search(self, prefix):
        root = self.root
        for p in prefix:
            if p not in root.children:
                return []
            root = root.children[p]
        # walk down the trie following the prefix
        # return all words that start with prefix
        words = []
        self._collect_words(root, prefix, words)
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

print(trie.search("ca"))  # ["cat", "car", "card", "care"]
Show less

One — Why is Trie search faster than binary search for autocomplete?
Binary search needs a sorted list and takes O(log n) — so 100,000 words needs about 17 checks. But it can only find exact words, not prefixes.
A Trie finds all words starting with "car" in O(3) — just the length of the prefix. Three letters, three steps, done. It doesn't matter if there are 100 or 100,000 words stored. Binary search gets slower as the dictionary grows. Trie doesn't.

Two — What does is_end do and why would the Trie break without it?
Right instinct, sharpen it. Without is_end you can't tell where words stop. "card" and "care" both pass through "car" — without marking "car" as a valid word end, you'd never know "car" itself is a word. Every path would just keep going with no stopping point.
Three — Your _collect_words is recursive. What is its base case?
Correct. When is_end is True, you've found a complete word — add it to results. The recursion still continues into children to find longer words, but is_end is what triggers saving a word.


# Graphs 

a tree is just a graph with one rule: no cycles, one parent per node. Remove that rule and you get a graph. Nodes can connect to anything.
A graph is just this:
Alice ——— Bob
  |         |
Charlie — Diana
  |
 Eve
No root. No parent/child. Just nodes and connections — called edges.

The Data Structure — Queue
Which data structure does this naturally? Think about it — you visit Alice's friends first, then add their friends to check next. First people added, first people checked.
That's a queue. First in, first out. You learned this in Week 2.
Start: queue = [Alice]

Step 1: pop Alice → check her friends → add Bob, Charlie to queue
queue = [Bob, Charlie]

Step 2: pop Bob → check his friends → add Diana to queue
queue = [Charlie, Diana]

Step 3: pop Charlie → check his friends → add Diana, Eve to queue
queue = [Diana, Diana, Eve]   ← problem here — Diana twice

The Visited Set
You need to remember who you've already checked — otherwise you visit the same person twice and loop forever. 

The Graph Structure
A graph in Python is just a dictionary — each person maps to a list of their friends:
pythongraph = {
    "Alice":   ["Bob", "Charlie"],
    "Bob":     ["Alice", "Diana"],
    "Charlie": ["Alice", "Diana", "Eve"],
    "Diana":   ["Bob", "Charlie"],
    "Eve":     ["Charlie"]
}

use dqeue 

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

    queue.append((start, 0))   # (person, steps)
    visited.add(start)

    while queue:
        node, steps = queue.popleft()   # pop front

        if node == target:              # found it
            return steps

        for neighbour in graph[node]:   # check all friends
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, steps + 1))

    return -1   # not found

print(bfs(graph, "Alice", "Eve"))    # 2 steps — Alice→Charlie→Eve
print(bfs(graph, "Alice", "Diana"))  # 2 steps — Alice→Bob→Diana
print(bfs(graph, "Alice", "Alice"))  # 0 steps — already there


--always this mistake 
pythonqueue = append([start])      # ❌ append is a method, not a function
visited = append.(start)     # ❌ this means nothing in Python
Correct way:
pythonqueue.append(start)          # ✅ method on the deque
visited.add(start)           # ✅ sets use .add() not .append()

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

# dfs

DFS — stack — goes deep first — finds a path, not necessarily shortest

DFS is like exploring a maze by always turning left — you'll eventually find the exit but maybe not the fastest way out.

DFS — Depth First Search
Same graph, different approach. Instead of a queue — use a stack. Instead of exploring all neighbours first — dive as deep as possible down one path before trying another.
Graph:
Alice — Bob — Diana
  |              
Charlie — Eve
BFS explores: Alice → Bob, Charlie → Diana, Eve
DFS explores: Alice → Bob → Diana → backtrack → Charlie → Eve


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

    return -1

print(dfs(graph, "Alice", "Eve"))     # finds Eve — but steps may differ from BFS
print(dfs(graph, "Alice", "Diana"))
print(dfs(graph, "Alice", "Alice"))

# Dynamic programming 
The Two Approaches
Top-down — memoization. Start with the big problem, recurse down, cache results. You already know this.
Bottom-up — tabulation. Start with the smallest subproblems, fill a table upward until you reach the answer. No recursion at all.



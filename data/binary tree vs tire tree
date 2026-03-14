Next — Binary Trees
This is where everything connects. Recursion plus a new data structure.
A binary tree is just a recursive structure — each node has a value and up to two children. Left and right. Those children are also nodes with their own left and right. It goes as deep as needed.
        10
       /  \
      5    15
     / \     \
    3   7    20
Every node follows the same rule — value, left child, right child. Sound familiar? It's the folder problem again. A folder containing folders. Same shape, different name.

Before we code — one question:
Look at this tree:
        10
       /  \
      5    15
     / \     \
    3   7    20
If I asked you to print every number in the tree — how would you do it? You can't loop because you don't know how deep it goes.
What's your instinct?check if number is there and beyond that check for number and print all10:46 AMRecognized vague request and prepared structured explanationRecognized vague request and prepared structured explanationRight instinct — but let me make it precise because "check if number is there and beyond" is actually describing recursion without realising it.

What You're Actually Describing
"Check a number, then go beyond it and check again" — that IS recursion. You just described it in plain English.
The formal version:
to print all numbers in a tree:
    print the current node's value
    then do the same thing for the left child
    then do the same thing for the right child
The function calls itself on the left child, then on the right child. Each child is a smaller tree. Same problem, smaller scale.

The Base Case For Trees
What stops the recursion? When there's no node — when you reach an empty branch. In Python that's None.
        10
       /  \
      5    15
     / \     \
    3   7    20
Node 3 has no children — both are None. That's the base case.

Build a Tree Node in Python
A tree node is just a simple class:
pythonclass Node:
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

Your Task
Write a recursive function print_tree(node) that prints every value in the tree.
Two things to define before coding — answer these first:
One — what is the base case? When does the function stop?
Two — what are the two recursive calls? What does the function call itself on?
Answer those then write the code. No hints this time — you have everything you need from the folder counter and fibonacci.

Question 1 ✅ Correct. When you reach None — the end of a branch — there's nothing left to process. That's the base case. No node means stop.

Question 2 — Half right.
You said "values at the end — 3, 7, 20." Close but not complete. Moving print after the recursive calls is called post-order traversal. You print a node only after fully exploring everything beneath it. So the output would be:
3 7 5 20 15 10
Not just the leaf nodes. Every node gets printed — but only after its entire subtree is done. The deepest nodes print first, the root prints last.

Question 3 ❌ Not quite.
You said "tree has a path so either down or up." The real reason is simpler — tree traversal doesn't revisit nodes. Each node is visited exactly once, on a straight path down. Fibonacci revisits subproblems — fib(3) gets called multiple times from different branches. Trees don't have that problem because each node has exactly one parent. No repetition means no need to cache.

Week 3 — Complete
You've now covered:

Recursion ✅
Fibonacci + Memoization ✅
Binary Tree Traversal ✅
Pre-order vs Post-order ✅

A Trie (pronounced "try", also known as a prefix tree) is a specialized tree data structure used to store dynamically changing strings. The foundation of this data structure is the Trie Node.Unlike a binary tree node that only has a left and right child, a Trie node can have multiple children—one for each possible next character in a string.

Here is a breakdown of the standard Trie Node structure, the different ways to implement it, and code examples.Core Components of a Trie NodeA standard Trie node contains two essential pieces of information:
Children (children): A collection of references (pointers) to the node's children. Each child represents the next character in a word.

End of Word Flag (is_end_of_word): A boolean value that is set to True if the path from the root to this specific node represents a complete, valid word that was inserted into the Trie. If it is False, the node is merely a prefix for a longer word.(Note: The node usually does not need to store the character itself. The character is implicitly defined by the link/key that points to the node from its parent).Two Ways to Structure the childrenDepending on your memory constraints and the size of your alphabet, there are two primary ways to store the children in a Trie node:

1. Using an Array (Fastest, but uses more memory)If you know your data will only consist of lowercase English letters (a-z), you can use an array of fixed size (26).Pros: Lightning-fast $O(1)$ lookups. You just calculate the index (e.g., char - 'a').Cons: Wastes a lot of memory. Every single node creates an array of 26 pointers, even if it only has 1 child. It also doesn't scale well to Unicode or special characters.
2. Using a Hash Map / Dictionary (Space-efficient, handles any character)Instead of a fixed array, you use a Hash Map where the key is the character and the value is the next TrieNode.Pros: Highly memory efficient for sparse trees. It can easily handle any character (uppercase, numbers, emojis, Unicode) without changing the code.
Cons: Slightly slower than an array due to hash function overhead, though still conceptually $O(1)$.

The Binary Tree: A Fork in the Road
You are exactly right about the Binary Tree. The word "Binary" means two. Every time you are at a node in a Binary Tree, the path can only split in a maximum of two directions: Left or Right.

Think of it like a fork in the road where you have to choose to go either left or right.

The Trie: A Roundabout with 26 Exits
A Trie is what we call an N-ary Tree (meaning a node can have any number of children). Instead of just Left and Right, a Trie node can split into as many paths as there are characters in your alphabet.

If you are only using lowercase English letters, a single node in a Trie can split into 26 different paths at the exact same time—one for 'a', one for 'b', one for 'c', all the way to 'z'.

A Visual Example
Imagine we want to store the words "cat", "car", "cop", and "bat".

In a Trie, the top node (the Root) doesn't just split into two. It splits based on the first letter of our words. Here, it splits into 'c' and 'b'.

Then, look at the 'c' node. It splits into 'a' (for cat/car) and 'o' (for cop).

Plaintext
          [Root]
         /      \
       'c'      'b'     <-- The root splits into 'c' and 'b'
      /   \       \
    'a'   'o'     'a'   <-- The 'c' splits into 'a' and 'o'
    / \     \       \
  't' 'r'   'p'     't' <-- The 'a' splits into 't' and 'r'
Summary
Binary Tree Node: Has exactly left and right pointers (Max 2 splits).

Trie Node: Has a collection of pointers, one for every possible next letter (Max 26 splits for the English alphabet, or even thousands of splits if using Unicode/Emojis).
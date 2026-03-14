#in python there is foundational data structure and we are creating a trienode using 
#trie is a tree like data structure that stores a dynamic set of strings, 
# where the keys are usually strings. It is used for efficient retrieval of a key in a 
# large dataset of strings. Each node in the trie represents a single character of a string,
#  and the path from the root to a node represents a prefix of the string. 
# The trie can be used to store words, and it allows for fast prefix-based searching.
# Think of it like folders on your computer. If you want to spell the word "cat":

# You open the first dictionary and create a folder named "c".

# Inside the "c" folder (the value), you open a new dictionary and create a folder named "a".

# Inside the "a" folder (the value), you open another dictionary and create a folder named "t".

# If we look at just the dictionaries, it looks a lot like this:
# { "c" : { "a" : { "t" : {} } } }

# By nesting them this way, the computer can easily follow the chain of letters layer by layer to build or search for entire words.
from logging import root
from sys import prefix


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
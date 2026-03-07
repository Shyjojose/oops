# Exercise 1 — undo system
stack = []
stack.append("hello")
stack.append("world")
stack.append("python")
print("Original:", stack) # Output: python
print(" undo:", stack.pop()) #  Output: world
print("Current:", stack) # Output: hello, python
print(" undo:", stack.pop()) # Output: python
print("Current:", stack) # Output: hello

# Exercise 2 — valid parentheses
def is_valid(s):
    stack = []
    for i in s:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (i == ")" and top != "(") or (i == "}" and top != "{") or (i == "]" and top != "["):
                return False
    return len(stack) == 0  
    # your logic here
    # return True or False

print(is_valid("(())"))    # True
print(is_valid("({)}"))    # False
print(is_valid("({[]})"))  # True




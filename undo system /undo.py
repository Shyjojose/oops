stack=[]
for i in range(3):
    stack.append(str(input(f"Enter value for position {i}: "))) 
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

#pallindrome check 

def is_palindrome(s):
    stack =[]
    for i in s:
        stack.append(i)
        print(stack)
    for i in s:
        print(i)
        if i != stack.pop():
            return False
    return True     

print(is_palindrome("racecar"))  
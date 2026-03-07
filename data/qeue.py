from collections import deque

# que = deque()
# que.append("bob")
# que.append("alice")
# que.append("charlie")
# print("Original:", que)  # Output: bob, alice, charlie
# print(" dequeue:", que.popleft())  # Output: bob
# print("Current:", que)  # Output: alice, charlie
# print(" dequeue:", que.popleft())  # Output: alice
# print("Current:", que)  # Output: charlie

lis = ["bob", "alice", "charlie", "david"]
num = 2
que = deque(lis)
while len(que) > 1:
    for i in range(num):
        que.append(que.popleft())
        print("Current:", que)  # Output: charlie
    que.pop()
print("Last remaining:", que)  # Output: charlie

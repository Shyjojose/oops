# Exercise 1 — Simulate a coffee shop queue. Three customers join: "Alice", "Bob", "Charlie". Serve them one by one using popleft(). Print who gets served each time.
# Exercise 2 — Hot Potato game. Given a list of names and a number n, pass the "potato" around the queue n times. The person holding it after n passes gets eliminated. Keep going until one person is left — they win.

from collections import deque

que = deque()
que.append("bob")
que.append("alice")
que.append("charlie") #queue = (bob, alice, charlie)
print("Original:", que)  # Output: bob, alice, charlie
print(" dequeue:", que.popleft())  # Output: bob
print("Current:", que)  # Output: alice, charlie
print(" dequeue:", que.popleft())  # Output: alice
print("Current:", que)  # Output: charlie

lis = ["bob", "alice", "charlie", "david"]
num = 2
que = deque(lis)
while len(que) > 1:
    for i in range(num):
        que.append(que.popleft())
        print("Current:", que)  # Output: charlie
    que.popleft()
print("Last remaining:", que)  # Output: charlie

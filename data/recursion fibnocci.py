# One Thing To Notice — A Hidden Problem
# Your code works. But try running fib(40). It will be slow. Try fib(100). It might never finish.
# Here's why. Look at what happens when you call fib(5):
# fib(5)
# ├── fib(4)
# │   ├── fib(3)
# │   │   ├── fib(2) = 1
# │   │   └── fib(1) = 1
# │   └── fib(2) = 1
# └── fib(3)
#     ├── fib(2) = 1
#     └── fib(1) = 1
# fib(3) is calculated twice. fib(2) is calculated three times. For fib(40) the same tiny subproblems get recalculated millions of times. That's O(2ⁿ) — exponentially slow.

# The Fix — Memoization
# Remember Week 1? "Never solve the same problem twice." That's exactly what memoization does — store results you've already calculated.
# pythondef fib(n, memo={}):
#     if n == 1 or n == 2:
#         return 1
#     if n in memo:
#         return memo[n]      # already calculated — return instantly
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)  # store it
#     return memo[n]
# Now fib(3) is calculated once, stored, never recalculated again. O(n) instead of O(2ⁿ).

# Your task — rewrite your fibonacci using memoization. Test these:
# pythonprint(fib(5))    # 5
# print(fib(10))   # 55
# print(fib(50))   # 12586269025 — instant, not slow
# Write it and paste back. This is the bridge between Week 3 recursion and Week 9 dynamic programming — you're learning it early because it matters everywhere.
def fibnocci(n,memo = {}):
	#base case
	if n== 1:
		return 1 
	
	if n==2:
		return 1
	#recursive case
	if n in memo:
		return memo[n]
	memo[n] = fibnocci(n-1, memo) + fibnocci(n-2, memo)
	return memo[n]


print(fibnocci(10))
print(fibnocci(5))
print(fibnocci(50))


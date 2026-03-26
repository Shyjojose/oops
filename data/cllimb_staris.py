def climb_stairs(n):
    if n == 1:
        return 1
    table = [0] * (n + 1) # this make list of size n+1 with all elements as 0 [0,0,0,..n+1 times]
    table[1] = 1
    table[2] = 2
    for i in range(3, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(climb_stairs(1))    # 1
print(climb_stairs(2))    # 2
print(climb_stairs(3))    # 3
print(climb_stairs(4))    # 5
print(climb_stairs(5))
print(climb_stairs(10))   # 89
print(climb_stairs(89))

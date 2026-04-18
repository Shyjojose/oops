>Knapsack Problem 
Every resource allocation decision -budget planning feature selection use this pattern 

problem 
You're a thief. You have a bag that holds 10kg. There are 4 items:
Item     Weight   Value
─────────────────────────
Laptop     3kg     £4000
Phone      1kg     £1000  
Camera     4kg     £3000
Tablet     5kg     £2000

you want to maximize vlaue without exceeding 10 kg 

Greedy thingking take the most valuable first. Laptop 4000 camera 3000 phone 1000 8kg but is that the best?

The DP Table
You build a 2D table. Rows are items, columns are weight capacities from 0 to 10.
Each cell answers: "what is the maximum value using the first i items with capacity j?"
        0  1  2  3  4  5  6  7  8  9  10
──────────────────────────────────────────
none    0  0  0  0  0  0  0  0  0  0  0
Laptop  0  0  0  4  4  4  4  4  4  4  4
Phone   0  1  1  4  5  5  5  5  5  5  5
Camera  0  1  1  4  5  5  5  7  8  8  8
Tablet  0  1  1  4  5  5  5  7  8  8  8

The Decision At Each Cell
For every item and every capacity you ask two questions:
Can I take this item? — does it fit in the current capacity?
Should I take it? — is it better to take it or leave it?
python# leave it — same value as without this item
leave = table[i-1][j]

# take it — this item's value + best value with remaining capacity
take = values[i] + table[i-1][j - weights[i]]

table[i][j] = max(leave, take)

Before You Code — Trace This
For the Phone (weight=1, value=£1000) at capacity 3:

Can we take it? Yes — 1 ≤ 3
Leave it → table[Laptop][3] = 4000
Take it → 1000 + table[Laptop][3-1] = 1000 + table[Laptop][2] = 1000 + 0 = 1000
Best → max(4000, 1000) = 4000

So we leave the phone at capacity 3 because the laptop alone is worth more.

Your task — answer these before coding:
One — At capacity 4 with Phone available, should we take Phone + Laptop or just Camera? Trace it.
Two — What are the base cases for the 2D table?


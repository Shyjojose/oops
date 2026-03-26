# Given coins [1, 5, 10, 25] and an amount 36, what is the 
# minimum number of coins to make that amount?

 # https://youtu.be/KnWorqyDSLA?si=FPbfG8j1xXhAFR1Z

#the coins 1+5+25+5 = 36

def min_coins(coins, amount):
    table = [float('inf')] * (amount + 1) # this make list of size amount+1 with all elements as infinty
    table[0] = 0 # base case: 0 coins needed to make amount
    for i in range(1, amount + 1): # iterate through all amounts from 1 to amount
        for coin in coins:
            if coin <= i: # if the coin value is less than or equal to the current amount
                table[i] = min(table[i], table[i - coin] + 1) #i - coin check the befor position liek i=10 10-5 = 5 and table[5] is 1 so table[10] will be min(infinity, 1+1) = 2
    return table[amount] if table[amount] != float('inf') else -1 # if the amount cannot be made with the given coins, return -1



## Mathematical/computer programming problems from Project Euler

## Set global variables as lists to define the coins/values and target amount
coins = [1, 2, 5, 10, 20, 50, 100, 200]  ## Coin values in pence
target_amount = 200  ## Target amount in pence (£2)

## Define a function with lists to store the number of ways to make each amount.
def countWaysToMakeAmount(target_amount, coins):
    ## This initialises a list called "ways" with "target_amount" list + 1.
    ## The list stores the number of ways to make each amount from 0 to "target_amount" using the given coins.
    ## Each index in the ways list corresponds to an amount in pence.
    ways = [0] * (target_amount + 1)
    
    ## Initially, all values are set to 0 because we haven't calculated any combinations yet.
    ## There's one way to make 0p: use no coins.
    ways[0] = 1  

## Program to loop through each coin
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            ways[amount] += ways[amount - coin]
    return ways[target_amount]

## Calculate the number of ways to make £2 and print
number_of_ways = countWaysToMakeAmount(target_amount, coins)
print(f"The number of different ways to make £2 is: {number_of_ways}")

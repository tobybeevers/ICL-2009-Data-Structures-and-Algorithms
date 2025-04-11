"""
Module:      ICL-2009 Data Structures & Algorithms
Assignment:  Lab Task 4
Program:     Coin Change Variations Calculator
Description: This program calculates the number of ways to form a target amount (in pence)
             using UK coin denominations. The algorithm is based on a dynamic programming 
             approach similar to Project Euler Problem 31.
Version:     V1 01/02/2025 by Toby Beevers
Test Cases:
Make sure to test this program with a variety of inputs, such as:
1. Negative numbers
    Entry = -2        
    Result = print("Invalid input: The amount cannot be negative.")
2. Non-integer inputs (e.g., strings)
    Entry = "abc""        
    Result = print(""Invalid input: could not convert string to float."")
3. Valid target amount (e.g., 1 pound £)
    Entry = 1           
    Result = print("The number of different ways to make £1.00 is: 4563")
4. Edge case of 0 pounds
    Entry = 0           
    Result = print("The number of different ways to make £0.00 is: 1")
5. Valid target amount with decimal value (e.g., 2.5 pounds)
    Entry = 2.5
    Result = print("The number of different ways to make £2.50 is: 200187")
"""
class Colors:
    GREEN = '\033[32;1m'
    RED = '\033[31;1m'
    YELLOW = '\033[33;1m'
    END = '\033[0m'
class Styles:
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def count_ways_to_make_amount(target_amount, coins):
    if target_amount < 0:
        raise ValueError("Target amount cannot be negative.")
    ways = [0] * (target_amount + 1)
    ways[0] = 1
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            ways[amount] += ways[amount - coin]
    return ways[target_amount]

def main_program():
    print(f"{Styles.BOLD}{Colors.GREEN}Welcome to the UK Coin Change Calculator!{Colors.END}{Styles.END}")
    print(f"{Styles.ITALIC}{Colors.RED}To start, enter a target amount in pounds (e.g., 2 for £2).{Colors.END}{Styles.END}")
    while True:
        user_input = input("Enter the target amount in pounds or 'exit' to quit: ").strip()

        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        try:
            target_pounds = float(user_input)
            if target_pounds < 0:
                raise ValueError("The amount cannot be negative.")
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            continue
        target_amount = round(target_pounds * 100)
        number_of_ways = count_ways_to_make_amount(target_amount, COINS)
        print(f"The number of different ways to make £{target_pounds:.2f} is: {number_of_ways}\n")
if __name__ == '__main__':
    main_program()

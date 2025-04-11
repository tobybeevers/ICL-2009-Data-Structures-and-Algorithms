"""
Module:      ICL-2009 Data Structures & Algorithms
Assignment:  Lab Task 1
Program:     Program One Prime Number Checker
Description: This program .
Version:     V1 01/10/2024 by Toby Beevers
             V2 01/02/2025 by Toby Beevers
Test Cases:
Make sure to test this program with a variety of inputs, such as:
1. Negative numbers
    Entry = 0.5         
    Result = print("Invalid input. Please enter a number below 100.")
2. Non-integer inputs (e.g., strings)
    Entry = TEXT        
    Result = print("Invalid input. Please enter a number below 100.")
3. Valid prime numbers (e.g., 2, 3, 5, 7)
    Entry = 2           
    Result = print("The number 2 is a Prime Number."), in Green color
4. Valid composite numbers (e.g., 4, 6, 8, 9)
    Entry = 4           
    Result = print("The number 4 is NOT a Prime Number."), in Red color
5. Edge cases like 0 and 1
    Entry = 0           Result = print("The number 0 is NOT a Prime Number.")
    Entry = 1           Result = print("The number 1 is NOT a Prime Number.")
"""
# Create Classes for colours and Styles
class colors:
  GREEN = '\033[32;1m'
  RED = '\033[31;1m'
  END = '\033[0m'
class styles:
  ITALIC = '\033[3m'
  UNDERLINE = '\033[4m'
  BOLD = '\033[1m'
  END = '\033[0m'

## Create list with the prime numbers 0 to 100
primeNumbers = ["2","3","5","7","11","13","17","19","23","29","31","37","41","43","47","53","59","61","67","71","73","79","83","89","97"]

## Print the Welcome message
print()
print(f"{styles.BOLD}{colors.GREEN}Welcome to my Prime Number Checker{colors.END}{styles.END}")


## Main Program
def main():
    while True:  ## Loop to allow continuous checking until user exit
        print()
        userInput = input('Enter a number below 100 to check (or type "exit" to quit): ')
        print()
        
        ## Validation to print goodbye if the user choses to exit the program
        if userInput.lower() == 'exit':
            print("Goodbye!")
            print()
            break  

        ## Validate input, must be a int below 101 die to list only being to 100
        ## Skips the rest of the loop and ask for input again
        if not userInput.isdigit() or int(userInput) >= 100:
            print("Invalid input. Please enter a number below 100.")
            continue

        found = False  ## Stores and resets found for each user input
        for i in primeNumbers:
            if i == userInput:
                found = True
                break

        if found:
            print()
            print(colors.GREEN + f"The number {userInput} is a Prime Number." + colors.END)
            print()
        else:
            print()
            print(colors.RED + f"The number {userInput} is NOT a Prime Number." +colors.END)
            print()
main()
## Test Cases
## Make sure to test this program with a variety of inputs, such as:

  ## Negative numbers
      ## Entry = 0.5         
      ## Result = print("Invalid input. Please enter a positive integer.")

  ## Non-integer inputs (e.g., strings)
      ## Entry = TEXT        
      ## Result = print("Invalid input. Please enter a positive integer.")

  ## Valid prime numbers (e.g., 2, 3, 5, 7)
      ## Entry = 2           
      ## Result = print("The number 2 is a Prime Number."), in Green color

  ## Valid composite numbers (e.g., 4, 6, 8, 9)
      ## Entry = 4           
      ## Result = print("The number 4 is NOT a Prime Number."), in Red color

  ## Edge cases like 0 and 1
      ## Entry = 0           Result = print("The number 0 is NOT a Prime Number.")
      ## Entry = 1           Result = print("The number 1 is NOT a Prime Number.")

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

## Print the Welcome message
print()
print ('Welcome to my Prime Number Checker V2')
print()

## Main Program
def main():
    while True:  ## Loop to allow continuous checking until user exits program
        userInputOrg = input('Enter a number (or type "exit" to quit): ')
        
        ## Validation to print goodbye if the user choses to exit the program
        if userInputOrg.lower() == 'exit':
            print("Goodbye!")
            print()
            break  
        
        ## Validation on input, must be a positive integer
        if not userInputOrg.isdigit():
            print()
            print("Invalid input. Please enter a positive integer.")
            print()
            continue    
        
        ## Convert user input to an integer, and set a variable to True
        userInput = int(userInputOrg)  
        found = True
        
        ## Validation to make sure the user input is greater than 1
        if userInput <2:
            found = False
        else:          
          
        ## For Loop starts with a check for factors
          for i in range(2, int(userInput**0.5)+1):
            if (userInput % i) == 0:
              found = False
              break
        ## NOTES
        ## The modulus operator (%) returns the remainder of the division of userInput
        ## If the result is 0, it means it divides userInput evenly, indicating that    
        ## userInput is not a prime number (since it has a divisor other than 1 and
        ## itself).

        if found:
            print()
            print(colors.GREEN + f"The number {userInput} is a Prime Number." + colors.END)
            print()
        else:
            print()
            print(colors.RED + f"The number {userInput} is NOT a Prime Number." +colors.END)
            print()
main()
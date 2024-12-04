## Test Cases
## Make sure to test this program with a variety of inputs, such as:

  ## Negative numbers
      ## Entry = 0.5         
      ## Result = print("Invalid input. Please enter a positive whole number.")

  ## Non-integer inputs (e.g., strings)
      ## Entry = TEXT        
      ## Result = print("Invalid input. Please enter a positive whole number.")

  ## Valid prime numbers (e.g., 2, 3, 5, 7)
      ## Entry = 2           
      ## Result = print("The number 2 is a Prime Number."), in Green color

  ## Valid composite numbers (e.g., 4, 6, 8, 9)
      ## Entry = 4           
      ## Result = print("The number 4 is NOT a Prime Number."), in Red color

  ## Edge cases like 0 and 1
      ## Entry = 0           Result = print("The number 0 is NOT a Prime Number.")
      ## Entry = 1           Result = print("The number 1 is NOT a Prime Number.")

  ## Test extremely Large Number 
      ## Entry = 26587659
      ## Result = print("The number 4 is NOT a Prime Number."), in Red color

# Create Classes for colours and Stylesclass colors:
# Classes for colors and styles
class colors:
    GREEN = '\033[32;1m'
    RED = '\033[31;1m'
    END = '\033[0m'
class styles:
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'

# This is a Dictionary to store the calculated numbers
# Using a HashTable to store already search numbers, this uses a 
prime_cache = {}

# Function to check if a number is prime
def is_prime(number):
    if number in prime_cache:
        return prime_cache[number]
    
    if number < 2:
        return False
    elif number % 2 == 0 and number != 2:
        result = False
    else:
        result = True
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                result = False
                break
                
    prime_cache[number] = result
    return result

# Main program
def main():
    while True:
      # Print the Welcome message
      print()
      print("Welcome to my Prime Number Checker V3")
      print(styles.ITALIC + "You can now enter up to 10 different numbers for me to check" + styles.END)
      print()   

      # Array to store up to 10 numbers
      user_numbers = []  

      # Collect up to 10 numbers from the user
      while len(user_numbers) < 10:
          user_input_org = input(f"Enter number {len(user_numbers) + 1} (or type 'done' to finish): ")

          # Allow the user to stop entering numbers early
          if user_input_org.lower() == 'done':
              break

          # Validate input to ensure it's a positive integer
          if not user_input_org.isdigit():
              print()
              print(colors.RED + "Invalid input. Please enter a positive whole number." + colors.END)
              print()
              continue

          user_input = int(user_input_org)
          user_numbers.append(user_input)  # Add the valid number to the array

      # Check each number in the array and print whether it's prime
      print(styles.UNDERLINE + "\nResults:" + styles.END)
      for number in user_numbers:
          if is_prime(number):
              print(colors.GREEN + f"The number {number} is a Prime Number." + colors.END)
          else:
              print(colors.RED + f"The number {number} is NOT a Prime Number." + colors.END)
    
      print("\nThank you for using the Prime Number Checker V3!")
      print (prime_cache)

      # Ask if the user wants to run the program again
      repeat = input("\nWould you like to check another set of numbers? Type 'stop' to end or press Enter to continue: ")
      if repeat.lower() == 'stop':
          print()
          print(styles.UNDERLINE + "Goodbye!" + styles.END)
          print()
          break

main()

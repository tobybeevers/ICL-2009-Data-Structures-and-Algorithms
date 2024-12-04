class Colors:
    GREEN = '\033[32;1m'
    RED = '\033[31;1m'
    END = '\033[0m'

class Styles:
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Cache for already checked numbers
prime_cache = {}

def is_prime(number):
    """Check if a number is prime and cache the result."""
    if number in prime_cache:
        return prime_cache[number]
    
    if number < 2:
        result = False
    elif number == 2:
        result = True
    elif number % 2 == 0:
        result = False
    else:
        result = all(number % i != 0 for i in range(3, int(number**0.5) + 1, 2))

    prime_cache[number] = result
    return result

def get_user_numbers():
    """Collect up to 10 numbers from the user."""
    user_numbers = []
    while len(user_numbers) < 10:
        user_input = input(f"Enter number {len(user_numbers) + 1} (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        if not user_input.isdigit():
            print(colors.RED + "Invalid input. Please enter a positive whole number." + colors.END)
            continue

        user_numbers.append(int(user_input))
    return user_numbers

def display_results(user_numbers):
    """Display the results of the prime number check."""
    print(Styles.UNDERLINE + "\nResults:" + Styles.END)
    for number in user_numbers:
        if is_prime(number):
            print(Colors.GREEN + f"The number {number} is a Prime Number." + Colors.END)
        else:
            print(Colors.RED + f"The number {number} is NOT a Prime Number." + Colors.END)

def main():
    """Main program loop."""
    while True:
        print("\nWelcome to my Prime Number Checker V3")
        print(Styles.ITALIC + "You can now enter up to 10 different numbers for me to check" + Styles.END)
        
        user_numbers = get_user_numbers()
        display_results(user_numbers)

        print("\nThank you for using the Prime Number Checker V3!")
        print(prime_cache)

        repeat = input("\nWould you like to check another set of numbers? Type 'stop' to end or press Enter to continue: ")
        if repeat.lower() == 'stop':
            print(Styles.UNDERLINE + "Goodbye!" + Styles.END)
            break

if __name__ == "__main__":
    main()

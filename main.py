def generate_fibonacci_up_to(limit):
    """Generate Fibonacci numbers up to a given limit."""
    fib_sequence = [0, 1]
    while fib_sequence[-1] < limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def find_closest_fibonacci(number):
    """Find the closest Fibonacci number to the given number."""
    fib_sequence = generate_fibonacci_up_to(number * 2)
    closest = fib_sequence[0]
    for fib in fib_sequence:
        if abs(fib - number) < abs(closest - number):
            closest = fib
    return closest

def main():
    """Main function to take user input and return the closest Fibonacci number."""
    while True:
        try:
            user_input = input("Enter a positive integer (or type 'exit' to quit): ")
            if user_input.lower() == "exit":
                print("Exiting the program.")
                break
            user_input = int(user_input)
            if user_input <= 0:
                print("Please enter a positive integer.")
                continue
            closest_fib = find_closest_fibonacci(user_input)
            print(f"The closest Fibonacci number to {user_input} is {closest_fib}.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()

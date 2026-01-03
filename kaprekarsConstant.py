def kaprekar_routine(num):
    """
    Perform one iteration of the Kaprekar routine.
    Returns the result of: (largest arrangement - smallest arrangement)
    """
    # Convert to 4-digit string with leading zeros if needed
    digits = str(num).zfill(4)
    
    # Sort digits in descending order (largest)
    largest = int(''.join(sorted(digits, reverse=True)))
    
    # Sort digits in ascending order (smallest)
    smallest = int(''.join(sorted(digits)))
    
    # Subtract
    result = largest - smallest
    
    return result, largest, smallest

def kaprekar_constant(num):
    """
    Demonstrate Kaprekar's constant (6174) by repeatedly applying the routine.
    """
    KAPREKAR_CONSTANT = 6174
    
    
    
    
    # Validate input
    if num < 0 or num > 9999:
        return None, "Number must be between 0 and 9999"
    
    # Check if all digits are the same (these don't work)
    digits = str(num).zfill(4)
    if len(set(digits)) == 1:
        return None, "Number must have at least two different digits"
    
    iterations = []
    current = num
    
    print(f"Starting number: {num}")
    print("-" * 50)
    
    step = 0
    while current != KAPREKAR_CONSTANT and step < 10:
        result, largest, smallest = kaprekar_routine(current)
        step += 1
        
        print(f"Step {step}: {largest} - {smallest} = {result}")
        iterations.append((largest, smallest, result))
        
        current = result
        
        # Check if we've reached the constant
        if current == KAPREKAR_CONSTANT:
            print(f"\n✓ Reached Kaprekar's constant {KAPREKAR_CONSTANT} in {step} steps!")
            return iterations, "Success"
    
    if current == KAPREKAR_CONSTANT:
        return iterations, "Success"
    else:
        return iterations, "Did not converge"

def main():
    print("=" * 50)
    print("KAPREKAR'S CONSTANT (6174) DEMONSTRATION")
    print("=" * 50)
    print("\nThe Kaprekar routine:")
    print("1. Take a 4-digit number (with at least 2 different digits)")
    print("2. Arrange digits in descending order")
    print("3. Arrange digits in ascending order")
    print("4. Subtract the smaller from the larger")
    print("5. Repeat with the result")
    print("6. You'll always reach 6174!\n")
    print("=" * 50)
    print("(Type 'exit' to quit)\n")
    
    while True:
        try:
            user_input = input("Enter a 4-digit number (or any number 0-9999): ")
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            number = int(user_input)
            
            print()
            iterations, status = kaprekar_constant(number)
            
            if iterations is None:
                print(f"Error: {status}")
            
            print()
            
        except ValueError:
            print("Error: Please enter a valid integer or 'exit' to quit!\n")
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()

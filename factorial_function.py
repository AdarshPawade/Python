def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer whose factorial is to be calculated
        
    Returns:
        int: The factorial of n
           
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Calculate factorial using recursive approach.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


# Test the functions
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 7, 10]
    
    print("Testing factorial function:")
    for num in test_numbers:
        try:
            result = factorial(num)
            print(f"factorial({num}) = {result}")
        except (ValueError, TypeError) as e:
            print(f"Error for factorial({num}): {e}")
    
    print("\nTesting recursive factorial function:")
    for num in test_numbers:
        try:
            result = factorial_recursive(num)
            print(f"factorial_recursive({num}) = {result}")
        except (ValueError, TypeError) as e:
            print(f"Error for factorial_recursive({num}): {e}")
    
    # Interactive testing
    try:
        user_input = int(input("\nEnter a number to calculate its factorial: "))
        print(f"factorial({user_input}) = {factorial(user_input)}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Error: {e}")

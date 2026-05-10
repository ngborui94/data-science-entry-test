def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return

    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return "Both inputs must be numeric."
    
    if divisor == 0:
        return "Division by zero is not allowed."
    
    return num % divisor == 0

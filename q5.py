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

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

# Scenario 1
result1 = check_divisibility(10, 2)
print(result1)

# Scenario 2
result2 = check_divisibility(7, 3)
print(result2)

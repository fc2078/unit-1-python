# Ex 1: Divide
def divide(a, b):
    """Divides two numbers, handling potential division by zero.

    Args:
      a: The numerator.
      b: The denominator.

    Returns:
      The quotient, or None if b is zero.
    """
    if b == 0:
        return None
    else:
        return a / b


# Divide the numbers
divide(3, 1)

# Assertions for divide function
assert divide(10, 2) == 5
assert divide(10, 0) is None


# Ex 2: Factorial
def factorial(n):
    """Calculates the factorial of a non-negative integer.

    Args:
      n: A non-negative integer.

    Returns:
      The factorial of n.
    """
    # Assert that n is POSITIVE
    assert n >= 0
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Find the factorial of number
factorial(5)

# Assertions for factorial function
assert factorial(0) == 1
assert factorial(5) == 120


# Ex 3: String Reverse
def reverse_string(string):
    """Reverses a given string.

    Args:
      string: A string to be reversed.

    Returns:
      The reversed string.
    """

    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


# Reverse the string
reverse_string("hello")

# Assertions for reverse_string function
assert reverse_string("hello") == "olleh"
assert reverse_string("") == ""


# Ex 4: Fibonacci
def fibonacci(n):
    """Generates the nth Fibonacci number.

    Args:
      n: The index of the Fibonacci number to calculate.

    Returns:
      The nth Fibonacci number.
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Find the nth Fibonacci number
fibonacci(5)

# Assertions for fibonacci function
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5

# Ex 5: Email Validation
# Import
import re


def is_valid_email(email):
    """Determines whether email is valid or not

    Args:
      email: The email to validate

    Returns:
      Boolean value if email is valid
    """
    email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
    return re.match(email_regex, email) is not None


# Validate the email
is_valid_email("test@example.com")


# Assertions for is_valid_email function
assert is_valid_email("test@example.com") is True
assert is_valid_email("invalid_email") is False

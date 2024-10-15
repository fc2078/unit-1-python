# Identify the potential errors in the following code snippets and modify them to include appropriate try/except blocks to handle exceptions gracefully.


# Ex 1: Division
def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)


# Example usage:
# Try to divide by 0 or other numbers
try:
    # Divisor cannot be 0
    divide_numbers(10, 0)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    # Try a different divisor
    divide_numbers(10, 2)
    print("Division operation completed with 2.")


# Ex 2: Opening Files
def read_file(filename):
    file = open(filename, "r")
    contents = file.read()
    print("File contents:", contents)
    file.close()


# Example usage:
# File not found since it is nonexistent
try:
    # Read a nonexistent file
    read_file("nonexistent.txt")
except FileNotFoundError:
    # Print this when exception occurs (inexistent file)
    print("Error: File not found.")


# Ex 3: List Items
def get_item(lst, index):
    item = lst[index]
    print("Item:", item)


# Example usage:
my_list = [1, 2, 3]
# IndexError: Index out of range
try:
    # Item 5 is nonexistent
    get_item(my_list, 5)
except IndexError:
    # Print since item not found (out of range)
    print("Error: Index out of range.")


# Ex 4: Dictionaries
def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)


# Example usage:
my_dict = {"a": 1, "b": 2}
# KeyError: 'c' | Invalid dictionary key
try:
    # Key c doesn't exist
    get_value(my_dict, "c")
except KeyError:
    # Print error due to invalid key
    print("Error: Invalid key.")
finally:
    # Use key b as it is existent
    get_value(my_dict, "b")
    print("Valid key returned!.")


# Ex 5: Else/Finally | Modify the following code to include an else block to execute code if no exceptions occur and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
def process_file(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    # If no errors are encountered
    else:
        print("No exceptions occurred.")
    # Finally, print this regardless
    finally:
        print("This action is always performed.")


# Example usage:
# Process inexistent file but handle errors whether present or not.
process_file("example.txt")

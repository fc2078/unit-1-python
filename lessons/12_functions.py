print()


# Task 1: Greeting | Write a function that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
# Function = welcome | Param: name
def welcome(name):
    # Print a greeting message using the provided name.
    print("Hello " + name + ", welcome to lesson 12!")


# Ask user to input name
# Variable = name
name = input("Enter your name: ")
print()

# Run the function with name
welcome(name)
print()


# Task 2: Square of a Number | Write a function that takes an integer as an argument and returns its square.
# Function = square | Param: sq_number
def square(sq_number):
    # Return the square of the provided number.
    return f"The square of {sq_number} is " + str(sq_number**2)


# Ask user to input number (input will be a float)
# Variable = sq_number
sq_number = float(input("Enter a number to find the square of: "))
print()

# Print the square of the provided number
print((square(sq_number)))
print()


# Task 3: Even or Odd | Write a function that takes a number as a argument that returns `True` if the number is even, and `False` otherwise.
# Function = even | Param: ev_number
def even(ev_number):
    # Return boolean value of result | True = even, False = odd
    return ev_number % 2 == 0


# Ask user to input number (input will be a int)
# Variable = ev_number
ev_number = int(input("Enter a number to check if it's even: "))
print()

# Print the result
print(even(ev_number))
print()


# Task 4: Area of a Rectangle | Write a function that takes the length and width of a rectangle and returns its area.
# Function = rectangle | Params: length, width
def rectangle(length, width):
    # Return the area of the rectangle using the provided length and width.
    return f"The area of the rectangle is: " + str(length * width)


# Ask user to input length and width (inputs are floats)
# Variables = length, width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print()

# Print the area
print((rectangle(length, width)))
print()


# Task 5: Celsius to Fahrenheit | Write a function that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit using the correct formula
def c_2_f(celsius):
    # Return the equivalent temperature in Fahrenheit using the provided Celsius temperature.
    return f"The equivalent temperature in Fahrenheit is: " + str(
        (celsius * 9 / 5) + 32
    )


# Ask user to input a temperature in Celsius (input is float)
# Variable = celsius
celsius = float(input("Enter a temperature in Celsius: "))
print()

# Print the equivalent temperature in Fahrenheit
print((c_2_f(celsius)))
print()


# Task 6: Average of Numbers | Write a function that takes a list of numbers and returns the average (mean) of those numbers.
# Function: mean | Param: nums
def mean(nums):
    # Return the average of the provided numbers using the sum and len functions.
    return f"The average of the numbers is: " + str(sum(nums) / len(nums))


# Ask user to input a list of numbers (inputs are floats, separated by comma via for loop)
# Variables: nums_input, nums
nums_input = input("Enter a list of numbers separated by commas: ")
nums = [float(num) for num in nums_input.split(",")]
print()

# Print the average of the provided numbers
print((mean(nums)))
print()


# Task 7: Total Calculator | Create a function that has arguments for the price and quantity of something, and returns the total.
def total_calculator(price, quantity):
    # Return the total cost of the items, including the discount if provided.
    total = price * quantity
    return f"The total cost of {quantity} items at ${price} each is ${total}"


# Ask the user to input a price and quantity
# Variables = price (float), quantity (int)
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
print()

# Print the total cost
print(total_calculator(price, quantity))
print()

## Calculatinator-inator 9000: Calculate two user-inputted numbers and perform various mathematical operations. MUST support float values.
# Welcome statement
print()
print("Welcome to the Calculatinator-inator 9000!")
print()
print(
    "I will calculate two numbers you input and perform any mathematical operation you desire."
)
print()

## User inputs numbers
# Variable = num_1 | User inputs first number
num_1 = float(input("Enter the first number: "))
print()
# Variable = num_2 | User inputs second number
num_2 = float(input("Enter the second number: "))
print()

## User inputs choice
# Print operation options
print("You have the following options for mathematical operations:")
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division (drops remainder of quotient)")
print("6. Exponent")
print("7. Remainder of quotient")
print()

# Variable = operation | User inputs the choice # of desired mathematical operation (float value)
operation = float(
    input(
        "Enter the NUMBER corresponding to the mathematical operation you would like to perform: "
    )
)

## Perform selected operation
# Addition
if operation == 1:
    print()
    print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}.")
# Subtraction
elif operation == 2:
    print()
    print(f"The difference between {num_1} and {num_2} is {num_1 - num_2}.")
# Multiplication
elif operation == 3:
    print()
    print(f"The product of {num_1} and {num_2} is {num_1 * num_2}.")
# Division
elif operation == 4:
    # Check for division by zero
    if num_2 != 0:
        print()
        print(f"The quotient of {num_1} divided by {num_2} is {num_1 / num_2}.")
    else:
        print()
        print("Error! Division by zero is not allowed. Try again.")
# Floor Division
elif operation == 5:
    print()
    print(
        f"The quotient (without the remainder) of {num_1} divided by {num_2} is {num_1 // num_2}."
    )
# Exponent
elif operation == 6:
    print()
    print(f"The result of raising {num_1} to the power of {num_2} is {num_1 ** num_2}.")
# Remainder of quotient
elif operation == 7:
    # Check for division by zero
    if num_2 != 0:
        print()
        print(f"The remainder of {num_1} divided by {num_2} is {num_1 % num_2}.")
    else:
        print()
        print("Error! Division by zero is not allowed. Try again.")
# Invalid choice returns error
elif operation < 1 or operation > 7:
    print()
    print("Error! Invalid choice. Please try again.")
print()

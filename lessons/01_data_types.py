## Task 1: Creating the float. Then, converting this float into an integer and printing the outputs.
# Variable = bazingas
bazingas = 5.32

# Print the bazingas, both the original and integer values
print()
print("Some numbers of bazingas:")
print(bazingas)
print(int(bazingas))
print()

## Task 2: Print output whether user-inputted number is positive, negative, or zero using if/else/elif satements
# Variable = positivity
positivity = float(
    input(
        "I will tell if your number is positive, negative, or zero. Enter a number : "
    )
)

# If/elif statements to determine number and output result.
if positivity > 0:
    print("You typed a positive number!")
elif positivity == 0:
    print("You typed zero!")
else:
    print("You typed a negative number!")

print()

## Task 3: Input two numbers, integer and float, perform math, and print results
# Variables = your_int, your_float | User will be given order of results
your_int = int(input("Enter an integer (no decimals) : "))
your_float = float(input("Enter a decimal number: "))
print()
print(
    "You will receive the results of your new number in this order: Addition, subtraction, multiplication, and division."
)

# Operations on variables
print(your_int + your_float)
print(your_int - your_float)
print(your_int * your_float)
print(your_int / your_float)
print()

## Task 4: Create dicitionary with keys being fruit names and values as quantities, and print the quanity of one fruit.
# Variable name = fruits
fruits = {
    "bananas": 5,
    "apples": 18,
    "oranges": 13,
    "pears": 4,
}

# Print the number of oranges
print("Here's a random number of oranges:")
print(fruits["oranges"])
print()

## Task 5 Create string var with a list of numbers and convert string into tuple and print out original string + tuple
# Variable name = num_list
num_list = "707, 717, 727, 737, 747, 757, 767, 777, 787"

# Create tuple and split by , | Variable name = num_tuple
num_tuple = tuple(map(int, num_list.split(", ")))

# Print result of original list and new tuple
print(
    "Here's a list of Boeing Jets sorted out by ascending numbers (7X7) with the original string and tuple of them:"
)
print(num_list)
print(str(num_tuple))
print()
print("That's all, folks!")

## Ex 1: Count how many spaces are in a given string
text = "Hello, world, my name is"
count = 0

for char in text:
    # Correction: Add a space in the string.
    if char == " ":
        count += 1
print(count)

## Ex 2: Determine if numbers 1 to n are even or odd
print("give me a number")
n = int(input())  # Correction: Use int() to convert the input to an integer.

# Correction: Append +1 to n to account for inputted number
for num in range(1, n + 1):
    # Correction: Use == to check if remainder is equal to 0.
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

# Ex 3: Calculate the factorial of a given number
num = int(input("Enter an integer: "))
# Correction: num < 0 will block all negative numbers.
if num < 0:
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num + 1):  # Correction: Include num in the range
        result *= i
    print(f"Factorial of {num} is {result}")

## Ex 4: Ask user to enter the correct password but only give them 3 attempts
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    # Correction: Set password equal to correct_password to use the correct password variable.
    if password == correct_password:
        print("Correct password!")
        # Correction: Add a break statement to exit the loop once the correct password is entered.
        break
    else:
        print("Incorrect password")
        # Extra: Try again.
        print("Try again.")

    # Correction: Set attempts equal to 3 to limit the number of attempts to strictly 3.
    if attempts == 3:
        print("Too many attempts")
        break

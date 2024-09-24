print("")

## Ex 1: Simple counter printing numbers from 1-10 using while loop
# Variable = simple_counter
simple_counter = 1
# While loop to print numbers from 1 to 10
while simple_counter <= 10:
    print(simple_counter)
    simple_counter += 1
print("")

## Ex 2: Counter reverse printing numbers from 10-1 using while loop
# Variable = reverse_counter
reverse_counter = 10
# While loop to print numbers from 10 to 1
while reverse_counter >= 1:
    print(reverse_counter)
    reverse_counter -= 1
print("")

## Ex 3: Calculate factorial of given number using while loop
# Variable = factorial | User inputs number to calculate factorial
factorial = int(input("Enter a number to calculate its factorial: "))
# While loop to calculate factorial
result = 1
while factorial > 1:
    result *= factorial
    factorial -= 1
print(f"The factorial of {4} is {result}.")
print("")

## Simple password guessing game using while loop. Ask user to guess predefined password and provide feedback.
# Variable = predefined_password | Define pwd
predefined_password = "farhan"
# Variable = guess | User guesses
guess = input("Guess the password: ")
# While loop to validate guess
while guess != predefined_password:
    print("Incorrect password! Try again.")
    guess = input("Guess the password: ")
print("Congratulations! You guessed the correct password.")
print("")

## Ex 5: Calculate sum of digits of a given number using FOR loop (Forlenza advised this was extra credit, must use a FOR loop instead)
# Variable = digits_number | User inputs number to calculate sum of digits
digits_number = int(input("Enter a number to calculate the sum of its digits: "))
# Variables = sum_digits, digit | Variables to store sum and current digit
sum_digits = 0
digit = 0
# For loop to calculate sum of digits
for digit in str(digits_number):
    sum_digits += int(digit)
print(f"The sum of the digits of {digits_number} is {sum_digits}.")
print("")

## Ex 6: Print first n numbers in the Fibonacci sequence using while loop (ALSO extra credit)
# Variable = n | User inputs number of Fibonacci numbers to print
n = int(input("Enter the number of Fibonacci numbers to print: "))

# Variables = fib_sequence, first_num, second_num | List to store Fibonacci sequence and first two numbers
fib_sequence = []
first_num = 0
second_num = 1

# While loop to generate Fibonacci sequence
while len(fib_sequence) < n:
    fib_sequence.append(first_num)
    first_num, second_num = second_num, first_num + second_num

# Print the Fibonacci sequence
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")
print("")

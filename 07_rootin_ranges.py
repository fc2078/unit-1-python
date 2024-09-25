print("")
## Ex 1: Write a program to print numbers from 1 to 10 using a for loop.
# Define variable and range in for loop. Print resulting range.
for x in range(1, 11):
    print(x)
print("")

## Ex 2: Write a program to count by 10s from 900 to 1000
# Define variable, range, and increment in for loop. Print resulting range.
for x in range(900, 1001, 10):
    print(x)
print("")

## Ex 3: Write a program counting from 1-100 by 9
# Define variable, range, and increment in for loop. Print resulting range.
for x in range(1, 101, 9):
    print(x)
print("")

## Ex 4: Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
# Variable = sum | Set sum
sum = 0
# Use for loop to iterate through numbers from 1 to 10
for x in range(1, 11):
    # Add each number to the sum
    sum += x
# Print the sum of all numbers from 1 to 10
print(sum)
print("")

## Ex 5: Run uncommenented code.
## Answer these questions:
## 1. What is the output?
## 2. Explain the iterative process that this code executes to get that output.
# Variable = rows | Set rows
rows = 5
# Nested for loop to print asterisks
for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
print("")

## Answers
# 1. The output is a pyramid of asterisks with 5 rows.
# 2. The iterative process in this code involves a nested for loop. The outer loop runs 5 times, and within each iteration, the inner loop runs i+1 times, printing 1 more asterisk per iteration.

# Ex 1: Check if integer is even and => 10. Print true if so or false if not
# Variable = the_ten
print("")
the_ten = 22
# Check integer
if the_ten % 2 == 0 and the_ten >= 10:
    print(True)
else:
    print(False)
print("")

# Ex 2: Determint ticket price based on age and student status. <18 OR student = $10, $20 otherwise
# Variables = student, age
student = False
age = 23
# Check for age/status of student
if age < 18 or student == True:
    print("Ticket price: $10")
else:
    print("Ticket price: $20")
print("")

# Ex 3: User inputs fruit name and check if in list. Print "Yes" if it is, "No" if it's not
# Variables = user_fruit, fruits
user_fruit = input("Enter a random fruit: ")
fruits = ["apple", "banana", "orange", "grapes", "pineapple"]
if user_fruit in fruits:
    print("")
    print("Yes, that fruit is in the list.")
else:
    print("")
    print("No, that fruit is not in the list.")
print("")

# Ex 4: Check if year is a century year AND a leap year
year = 2004

# HOLD at ex 4 due to cleanup


# '''
# Exercise 4:
# Check if a year is a century year and a leap year.
# '''

# '''
# Exercise 5:
# Calculate the cost of shipping for an online order based on the order weight and destination zone. 
# The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
# If the order weight is less than 0 kg, return an error message.
# '''

# '''
# Exercise 6:
# Determine the type of a triangle based on side lengths.
# Equilateral, Isosceles, Scalene, or Not a triangle.
# '''
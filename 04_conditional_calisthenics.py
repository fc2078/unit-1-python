# Ex 1: Check if integer is even and => 10. Print true if so or false if not
# Variable = the_ten
print("")
the_ten = 22
# If even and greater than or equal to 10
if the_ten % 2 == 0 and the_ten >= 10:
    print(f"{the_ten} is even and greater than or equal to 10.")
# If even but not greater than or equal to 10
elif the_ten % 2 == 0 and not the_ten >= 10:
    print("")
    print(f"{the_ten} is even but not greater than or equal to 10.")
# HOLD here due to 5th ending


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
# Variable = year
year = 2001
# Confirm both conditions are met
if year % 100 == 0 and year % 4 == 0:
    print("")
    print(f"Yes, {year} is a century year and a leap year.")

# If leap year but not a century year
elif year % 100 != 0 and year % 4 == 0:
    print("")
    print(f"Yes, {year} is a leap year but not a century year.")

# If a century year but not a leap year
elif year % 100 == 0 and year % 4 != 0:
    print("")
    print(f"Yes, {year} is a century year but not a leap year.")

# If neither century year nor a leap year
else:
    print("")
    print(f"No, {year} is not a century year or a leap year.")
print("")


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
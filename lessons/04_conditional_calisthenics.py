## Ex 1: Check if integer is even and => 10. Print true if so or false if not
# Variable = the_ten
print()
the_ten = 22
# If the number is even and greater than or equal to 10, print true
if the_ten % 2 == 0 and the_ten >= 10:
    print(True)
# Otherwise, print false
else:
    print()
    print(False)
print()

## Ex 2: Determint ticket price based on age and student status. <18 OR student = $10, $20 otherwise
# Variables = student, age
student = False
age = 23
# If less than 18 or student, print $10 ticket price
if age < 18 or student == True:
    print("Ticket price: $10")
# If above 18 or not student, print $20 ticket price
else:
    print("Ticket price: $20")
print()

## Ex 3: User inputs fruit name and check if in list. Print "Yes" if it is, "No" if it's not
# Variables = user_fruit, fruits
user_fruit = input("Enter a random fruit: ")
fruits = ["apple", "banana", "orange", "grapes", "pineapple"]
if user_fruit in fruits:
    print()
    print("Yes, that fruit is in the list.")
else:
    print()
    print("No, that fruit is not in the list.")
print()

## Ex 4: Check if year is a century year AND a leap year
# Variable = year
year = 2001
# Confirm both conditions are met
if year % 100 == 0 and year % 4 == 0:
    print()
    print(f"Yes, {year} is a century year and a leap year.")

# If leap year but not a century year
elif year % 100 != 0 and year % 4 == 0:
    print()
    print(f"Yes, {year} is a leap year but not a century year.")

# If a century year but not a leap year
elif year % 100 == 0 and year % 4 != 0:
    print()
    print(f"Yes, {year} is a century year but not a leap year.")

# If neither century year nor a leap year
else:
    print()
    print(f"No, {year} is not a century year or a leap year.")
print()

## Ex 5: Calculate cost of shipping for an online order based on the order weight and destination zone. $5/kg for Zone A and $7/kg for Zone B. Return error message if weight is less than 0 kg.
# Variables = weight, zone
weight = 3.22
zone = "A"
# Calculate based on Zone A
# Variable = cost_A
if zone == "A" and weight >= 0:
    cost_A = weight * 5
    print(f"The cost of shipping for your zone (Zone {zone}) order is: ${cost_A:.2f}")
# Calculate based on Zone B
# Variable = cost_B
elif zone == "B" and weight >= 0:
    cost_B = weight * 7
    print(f"The cost of shipping for your zone (Zone {zone}) order is: ${cost_B:.2f}")
# If weight is less than 0 kg, print error message
elif weight < 0:
    print()
    print("Error: Weight cannot be negative.")
print()

## Ex 6: Determine the type of a triangle based on side lengths. Equilateral, Isosceles, Scalene, or Not a triangle.
# Variables = side_1, side_2, side_3
side_1 = 5
side_2 = 3
side_3 = 4
#  Check if all sides are equal
if side_1 == side_2 == side_3:
    print("This is an equilateral triangle.")
# Check if any two sides are equal
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("This is an isosceles triangle.")
# If all sides are different
else:
    print("This is a scalene triangle.")
print()

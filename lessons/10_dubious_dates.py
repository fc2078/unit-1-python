## Import necessary modules/functions
from datetime import datetime

print()
## Exercise 1: Write a Python program that prints the current date and time using the datetime module.
# Varaible = current_datetime | Define variable as current date/time
current_datetime = datetime.now()

# Print current date/time
print(f"The current date and time is: {current_datetime}")
print()


## Exercise 2: Write a Python program that prints the current date and time using the datetime module, using the strftime function to format the date in standard U.S. date format (MM/DD/YYYY)
# Variable = current_datetime | Get current date and time
current_datetime = datetime.now()

# Variable = us_datetime | Format date and time into American format
us_datetime = current_datetime.strftime("%m/%d/%Y %-I:%-M %p")

# Print the formatted date and time
print("The current date and time (as the Americans say) is: " + us_datetime)
print()


## Exercise 3: Using the strptime function, convert two strings into dates. Then find the difference in days between the two.
# Variable = date1_str | Example date string 1
date1_str = "10/07/2024"

# Variable = date2_str | Example date string 2
date2_str = "02/21/2025"

# Variable = date1 | Convert string to date using strptime
date1 = datetime.strptime(date1_str, "%m/%d/%Y")

# Variable = date2 | Convert string to date using strptime
date2 = datetime.strptime(date2_str, "%m/%d/%Y")

# Variable = diff_days | Calculate difference in days between two dates
diff_days = (date2 - date1).days

# Print the difference in days
print(f"The difference in days between {date1_str} and {date2_str} is: {diff_days}")
print()

## Excercise 4: Write a program that asks the user for their birthdate and calculates their current age using the datetime module.
# Variable = birthdate_str | Ask the user for their birthdate
birthdate_str = input("Please enter your birthdate in this format: (MM/DD/YYYY): ")

# Variable = birthdate | Convert string to date using strptime
birthdate = datetime.strptime(birthdate_str, "%m/%d/%Y")

# Current date and time was previously defined and will not be defined again.

# Calculate current age
age = (
    current_datetime.year
    - birthdate.year
    - (
        (current_datetime.month, current_datetime.day)
        < (birthdate.month, birthdate.day)
    )
)

# Print the current age
print(f"Your current age is: {age}")

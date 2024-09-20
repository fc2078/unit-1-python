## Task 1: Check if user inputted correct pwd (NOT case sensitive)
# Define Function = check
# Variable = password
def check():
        # User inputs password
        password = str(input("Enter your password: "))
        # Check for validity + convert all characters to lowercase
        if password.lower() == "password":
            print("Correct password! Congratulations!")
        # Print incorrect and rerun func
        else:
            print("Incorrect Password! Try again.")
            check()
check()
print("")

## Task 2: Check if user input is empty. Print result based on input
# Define function = emptiness
# Variable = empty_string
def emptiness():
    #  User inputs empty string or any characters
    empty_string = str(input("Enter something: "))
    # Check if string is empty. Print invalid if so
    if empty_string == "":
         print("Invalid input!")
    # If string contains any characters
    else:
         print("Valid input!") 
emptiness()
print("")

## Task 3: User inputs sentence with the word "cat" used multiple times throughout. Each "cat" is replaced with "dog" regardless of capitalization
# Define function = dog_sentence
# Variable = cat_sentence
def dog_sentence():
     # User inputs sentence with "cat"
     cat_sentence = str(input("Enter a sentence using the word cat AT LEAST 3 times (where first letters are capitalized or not): "))
    # Replace all "cat" words with "dog" words abd print sentence
     dog_sentence = cat_sentence.replace("cat", "dog").replace("Cat", "Dog")
     print("")
     print(dog_sentence)
dog_sentence()
print("")
    
## Task 4: User inputs name and age and gets printed
# Define function = personal_info
# Variables = name, age
def personal_info():
     # User inputs name
     name = str(input("Enter your name: "))
     # User inputs age
     age = int(input("Enter your age: "))
     # Print name and age
     print("")
     print(f"Your name is {name} and your age is {age}!")
personal_info()
print("")

## Task 5: User inputs two floats and quotient is rounded to the nearest tenth and printed
# Define function = division
# Variables = dividend, divisor
def division():
     # User inputs dividend
     dividend = float(input("Enter a number: "))
     # User inputs divisor
     divisor = float(input("Enter a number to divide the previous number by: "))
     # Calculate quotient and round to nearest tenth
     quotient = round(dividend / divisor, 1)
     print("")
     print(f"The quotient is {quotient:.1f}")
division()
print("")
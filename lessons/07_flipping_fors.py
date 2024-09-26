print()
## Ex 1: Write a program to print each character of a given string using a for loop.
# Variable: stringer | Store string in variable
stringer = "I am so pro."
# Print each character in the string using a for loop
for char in stringer:
    print(char)
print()

## Ex 2: Write a program to calculate the sum of elements in a list using a for loop.
# Variable: numbers | Store list of numbers in variable
numbers = [8, 14, 23, 28, 34, 42, 49, 57]
# Calculate sum of elements and print the result
# Variable = 0 | Store sum of elements in variable
total = 0
for num in numbers:
    total += num
print(f"The sum of the numbers is: {total}")
print()

## Ex 3: Write a program to print the length of each word in a sentence using a for loop and a list.
# Variable: sentence | Store sentence in variable
sentence = str("This is some type of sentence.")
# Variable = word_length | Set word length
word_length = 0
# Variable = words | Split sentence into words
words = sentence.split()
# Print each word and its length using a for loop
print(f"Your sentence is: '{sentence}'")
print()
for word in words:
    print(f"The length of the word '{word}' is: {len(word)}")
print()


## Ex 4: Write a program that creates a dictionary (at least 4 key:value pairs) and then iterates through a dictionary and prints the result.
# Variable: train | Store dictionary in variable; some info about a train
train = {
    "fleet": "R142",
    "line": "5",
    "north_set": "6586-6590",
    "south_set": "7011-7015",
    "direction": "north",
    "time": "07:28",
    "origin": "FLA",
    "destination": "180",
}
# Print each key-value pair in the dictionary using a for loop
print(f"Here's a result for a random train line you requested:")
for key, value in train.items():
    print(f"{key}: {value}")
print()
print(
    "The car facing north is noted as the first north number, and the car facing south is the second south number"
)
print()

## Q: What do you notice about the output of your code? Is it what you expected?
# A: Most outputs are listed one line per iteration. What this means is that a new line is used for each character printed, word length printed, and the key-value pair printed. I was expecting this for the most part because it would be easier to list line by line.

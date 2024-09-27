## Todo Tracker in Service!
# Print welcome message and instructions
print()
print("Welcome to the Todo Tracker!")
print()
print("Here you can enter your tasks and keep track of them.")
print()
print("To add a new todo, type 'add' and then the task description.")
print()
print("To remove a todo, type 'remove' and then the name of the task.")
print()
print("To view the current list of todos, type 'view'.")
print()
print("To edit any todo, type 'edit'.")
print()
print("To clear the list of todos, type 'clear'.")
print()
print("To exit the program, type 'exit'")
print()
print("Let's get started.")
print()

# Initialize an empty list to store todo items. Define this list.
todos = []


## Define functions to handle user commands
# Function to add a new todo item
def add_todo(task):
    todos.append(task)
    print()
    print(f"{task} has been added to your list!")
    print()


# Function to remove a todo item
def remove_todo(task):
    if task in todos:
        todos.remove(task)
        print()
        print(f"{task} as been removed from your list!")
        print()
    else:
        print()
        print(f"{task} was not found in your list! Try again.")
        print()


# Function to view the current list of todos
def view_todos():
    if todos:
        print()
        print("Current list of todos:")
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")
    else:
        print()
        print("No todos found! Add something!")
        print()


# Function to edit a todo item
def edit_todo(task):
    if task in todos:
        new_task = input(f"What would you like to replace {task} with?: ")
        todos[todos.index(task)] = new_task
        print()
        print("Your todo has been updated!")
        print()
    else:
        print()
        print(f"{task} was not found in your list! Try again.")
        print()


# Function to clear the list of todos
def clear_todos():
    todos.clear()
    print()
    print("All todos have been cleared!")
    print()


## Present options to the user and handle their input
while True:
    user_input = input("Enter an action: add, remove, view, edit, exit: ").lower()
    if user_input == "add":
        task = input("What would you like to add?: ")
        add_todo(task)
    elif user_input == "remove":
        task = input("What would you like to remove?: ")
        remove_todo(task)
    elif user_input == "view":
        view_todos()
    elif user_input == "edit":
        task = input("What todo item would you like to edit?: ")
        edit_todo(task)
    elif user_input == "exit":
        print("Goodbye! Thanks for using the Todo Tracker.")
        print()
        break
    else:
        print("Invalid command! Please try again.")
print()

## Access todos file to read and write data
with open("todos.txt") as file:
    contents = file.readlines()
print(contents)


## FUTURE: Write functions in each command

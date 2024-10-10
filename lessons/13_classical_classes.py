print()


# Task 1: People Class | Define a class called Person with attributes name and age. Then, write a method within the class to introduce the person with their name and age. Create a new object using this new class, and call the method you created.
# Class: Person | Define a class called Person with attributes name and age
class Person:
    # Initialize objects with attributes name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to introduce the person with their name and age.
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."


# Create a new object using the Person class
person1 = Person("Yo mama", 21)

# Call the introduce method and print the statement
print(person1.introduce())
print()


# Task 2: Animals Speak | Create a base class Animal with a empty method called speak. Then create two subclasses, Dog and Cat, each with their own speak method. Create objects using these subclasses and call the speak method.
# Base class Animal with a empty method called speak
class Animal:
    # Create a new object using the Animal class and pass
    def speak(self):
        pass  # Added to avoid empty code error


# Subclass Dog with its own speak method
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Subclass Cat with its own speak method
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create objects using these subclasses and call the speak method
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print()


# """
# Task 3: Banking | Create a class BankAccount with attributes balance and owner. Include methods for depositing and withdrawing money, which should modify the balance attribute. Test these methods with instances of the class.
# """

# Parent class (base class)
class Animal:
    def __init__(self, name, age):
        self.name = name   # Property: Name of the animal
        self.age = age     # Property: Age of the animal

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (derived class) that inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call the constructor of Animal (parent class)
        self.breed = breed  # New property specific to Dog

    def bark(self):
        print(f"{self.name} is barking!")

# Another child class (derived class) that inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call the constructor of Animal (parent class)
        self.color = color  # New property specific to Cat

    def meow(self):
        print(f"{self.name} says meow!")

# Creating objects (instances) of Dog and Cat classes
dog1 = Dog("Buddy", 4, "Golden Retriever")
cat1 = Cat("Whiskers", 2, "Gray")

# Using methods from the classes
dog1.speak()    # Inherited from Animal
dog1.bark()     # Specific to Dog
print(f"{dog1.name} is {dog1.age} years old and is a {dog1.breed}.")

cat1.speak()    # Inherited from Animal
cat1.meow()     # Specific to Cat
print(f"{cat1.name} is {cat1.age} years old and has {cat1.color} fur.")

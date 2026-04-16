# Parent class representing a general Animal
class Animal:
    def __init__(self, name, age, health=50, happiness=50):
        # Common attributes shared by all animals
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        
    def display_info(self):
        # Display basic animal information
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")
    
    def feed(self):
        # Default feeding behavior
        self.health += 10
        self.happiness += 10
        print(f"Feeding {self.name}")


# Lion class inherits from Animal
class Lion(Animal):
    def __init__(self, name, age):
        # Call parent constructor
        super().__init__(name, age)
        # Additional attribute specific to Lion
        self.power = 100

    def feed(self):
        # Overriding feed method
        self.health += 15
        self.happiness += 20
        print(f"The Lion {self.name} feels powerful and happy after eating.")


# Tiger class inherits from Animal
class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.stripe = 50  # Unique attribute

    def feed(self):
        # Overriding feed method
        self.health += 12
        self.happiness += 12
        print(f"The Tiger {self.name} is looking sharp after the meal.")


# Bear class inherits from Animal
class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.wool = True  # Unique attribute

    def feed(self):
        # Overriding feed method
        self.health += 30
        self.happiness += 5
        print(f"The Bear {self.name} is getting ready for winter.")


# Zoo class to manage all animals
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []  # List to store animal objects
        self.name = zoo_name

    def add_animal(self, animal):
        # Add animal object to zoo list
        
        self.animals.append(animal)
        print(f"Added {animal.name} to {self.name}.")

    def print_all_info(self):
        # Print all animals information
        print("-" * 10, self.name, "-" * 10)
        for animal in self.animals:
            animal.display_info()
            
    def feed_all(self):
        # Feed all animals (Polymorphism happens here)
        print(f"\n--- Feeding time at {self.name}! ---")
        for animal in self.animals:
            animal.feed()


# Create Zoo object
my_zoo = Zoo("John's Awesome Zoo")

# Add animals
my_zoo.add_animal(Lion("Nala", 5))
my_zoo.add_animal(Lion("Simba", 7))
my_zoo.add_animal(Tiger("Rajah", 4))
my_zoo.add_animal(Bear("Baloo", 10))

# Display information before feeding
my_zoo.print_all_info()

# Feed all animals
my_zoo.feed_all()

# Display information after feeding
my_zoo.print_all_info()
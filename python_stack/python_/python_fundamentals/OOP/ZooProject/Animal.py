# Parent class representing a general Animal
class Animal:
    def __init__(self, name, age, health=0, happiness=0):
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

from animal import Animal
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

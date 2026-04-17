from animal import Animal

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

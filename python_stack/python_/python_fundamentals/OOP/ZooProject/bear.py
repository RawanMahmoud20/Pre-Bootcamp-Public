from animal import Animal


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



from animal import Animal
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


class Car:
    def __init__(self, color, engine, wheels = 4):
        self.color = color
        self.wheels = wheels
        self.engine = engine

    def print_info(self):
        print(f"My car has the color {self.color} and has {self.wheels} number of wheels")

# has-a

class Engine:
    def __init__(self, cylinder, horsepower):
        self.cylinder = cylinder
        self.horsepower = horsepower

bmw_engine = Engine(4, 200)
mercedes_engine = Engine(2, 150)

my_car = Car("red", bmw_engine, 3)
nesma_car = Car("blue", mercedes_engine)

my_car.print_info()
nesma_car.print_info()
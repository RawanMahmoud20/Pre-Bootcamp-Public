from zoo import Zoo
from lion import Lion
from tiger import Tiger
from bear import Bear
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
class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print("Initial Attributes: {a} ({b}) - Hunger: {c}, Energy: {d}".format(a=whiskers.name, b=whiskers.species, c=whiskers.hunger, d=whiskers.energy))
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2
whiskers.hunger-=3
whiskers.energy+=2
# TODO: Print Whiskers' modified attributes
print("Modified Attributes: {a} ({b}) - Hunger: {c}, Energy: {d}".format(a=whiskers.name, b=whiskers.species, c=whiskers.hunger, d=whiskers.energy))

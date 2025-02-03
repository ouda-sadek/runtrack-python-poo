# Creating class Animal
class Animal:
    # The constructor (__init__) initializes the "nom" and "age" attributes with default values
    def __init__(self):
        self.nom = ""
        self.age = 0

    # Method to age the animal (add 1 to age)
    def viellir(self):
        self.age += 1

    # Method to display the animal's name
    def nommer(self, nom):
        self.nom = nom
        print(f"L'animal se nomme {self.nom}.")

# Instantiating an Animal object
animal_1 = Animal()

# Display of the animal's initial age
print(f"L'age de l'animal  {animal_1.age} ans.")

# Ageing the animal
animal_1.viellir()

# Display of the animal's new age
print(f"L'age de l'animal maintenant {animal_1.age} ans.")

# Display of the animal's name
animal_1.nommer("Bobby")
    
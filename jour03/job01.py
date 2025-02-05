# Class Ville
class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    # Method to increase the number of inhabitants
    def ajouter_population(self):
        self.__habitants += 1

    # Method to obtain the number of inhabitants
    def get_habitants(self):
        return self.__habitants

# Class Personne
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    # Method to add a person to the city, increasing the population
    def ajouter_population(self):
        self.__ville.ajouter_population()

# Creation of City objects
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Display of the number of inhabitants of Paris and Marseille
print(f"Nombre d'habitants de Paris : {paris.get_habitants()}")
print(f"Nombre d'habitants de Marseille : {marseille.get_habitants()}")

# Creating Person objects
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Add people to cities
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Displaying the number of inhabitants after adding these people
print(f"Mise à jour de la population de Paris : {paris.get_habitants()}")
print(f"Nombre d'habitants de Marseille après : {marseille.get_habitants()}")

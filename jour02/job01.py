# Create class Rectangle
class Rectangle:
    def __init__(self, longueur, largeur):
        # Private attributes
        self.__longueur = longueur
        self.__largeur = largeur

    # Accessor for length
    def get_longueur(self):
        return self.__longueur

    # Accessor for width
    def get_largeur(self):
        return self.__largeur

    # Mutator for length
    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Mutator for width
    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Method to display rectangle dimensions
    def afficher(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")

# Creation of the rectangle with initial values
rect = Rectangle(10, 5)

# Display initial dimensions
rect.afficher()

# Changing dimensions
rect.set_longueur(12)
rect.set_largeur(8)

# Checking for changes rect.display()
rect.afficher()

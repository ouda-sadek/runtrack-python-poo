# Create class Livre
class Livre:
    def __init__(self, titre, auteur, nb_pages):
        # Private attributes
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        
    # Accessor for title
    def get_titre(self):
        return self.__titre
    
    # Accessor for author
    def get_auteur(self):
        return self.__auteur
    
    # Accessor for nb_pages
    def get_nb_pages(self):
        return self.__nb_pages
    
    # Mutator for title
    def set_titre(self, titre):
        self.__titre = titre

    # Mutator for author
    def set_auteur(self, auteur):
        self.__auteur = auteur

    # Mutator for nb_pages
    def set_nb_pages(self, nb_pages):
        # Check that nb_pages is a positive integer and that it is not negative integer
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Method to display book information
    def afficher(self):
        print(f"Titre : {self.__titre}, Auteur : {self.__auteur}, Nombre de pages : {self.__nb_pages}")

# Creating a book with the initial values
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)

# Displaying initial information
livre.afficher()

# Editing attributes
livre.set_titre("1984")
livre.set_auteur("George Orwell")

# Attempt to change page count (valid and invalid)
# Valid value
livre.set_nb_pages(328)
# Invalid value  
livre.set_nb_pages(-50)  

# Checking changes
livre.afficher()

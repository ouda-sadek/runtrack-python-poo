# Create class Livre
class Livre:
    def __init__(self, titre, auteur, nb_pages):
        # Private attributes
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        # private attribute, initialized to True by default
        self.__disponible = True
        
    # Accessor for title
    def get_titre(self):
        return self.__titre
    
    # Accessor for author
    def get_auteur(self):
        return self.__auteur
    
    # Accessor for nb_pages
    def get_nb_pages(self):
        return self.__nb_pages
    
    # Accessor for availability
    def get_disponible(self):
        return self.__disponible
    
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

    # Mutator for availability
    def set_disponible(self, disponible):
        self.__disponible = disponible

    # Method to display book information
    def afficher(self):
        print(f"Titre : {self.__titre}, Auteur : {self.__auteur}, Nombre de pages : {self.__nb_pages}, Disponible : {self.__disponible}") 

    # Method to check a availability
    def verification(self):
        """
        Checks if the book is available (if the available attribute is True).
        Returns True if the book is available, otherwise False.
        """
        return self.__disponible
    
    # Method to borrow a book
    def emprunter(self):
            """
            Allows you to borrow the book by making it unavailable.
            First check if the book is available without touching the _available attribute.
            """
            # checks that the book is available without using _available
            # If the book is not available
            if not self.verification():  
                print(f"Le livre '{self.__titre}' est déjà emprunté.")
                return False
            else:
                # The book becomes unavailable
                self.__disponible = False
                print(f"Vous avez emprunté le livre '{self.__titre}'.")
                return True
     
    # Method to return a book
    def rendre(self):
        """
        Allows you to return the book and make it available again.
        Check if the book has been borrowed before returning it.
        """
        # checks that the book is not available without using _available 
        # If the book is already available, it has not been borrowed  without using _available 
        if self.verification():
            print(f"Le livre '{self.__titre}' est déjà disponible.")
            return False
        else:
            # The book becomes available again
            self.__disponible = True
            print(f"Vous avez rendu le livre '{self.__titre}'.")
            return True
        
 

# Test 1 : Creating a book and checking its availability
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
livre1.afficher()  # Display book information
print(livre1.verification())  # Shows True, the book is available

# Test 2 : Borrow the book
livre1.emprunter()  # # Should make the book unavailable
livre1.afficher()  # Should show that the book is now unavailable

# Test 3 : Borrow a book that has already been borrowed
livre1.emprunter() # Should show that the book is already borrowed 

# Test 4 : Return the book
livre1.rendre()  # Should make the book available
livre1.afficher()  # Should show that the book is available again

# Test 5 : Make a book already available
livre1.rendre()  # Should show that the book is already available

#result
"""
Titre : Le Petit Prince, Auteur : Antoine de Saint-Exupéry, Nombre de pages : 96, Disponible : True
True
Vous avez emprunté le livre 'Le Petit Prince'.
Titre : Le Petit Prince, Auteur : Antoine de Saint-Exupéry, Nombre de pages : 96, Disponible : False
Le livre 'Le Petit Prince' est déjà emprunté.
Vous avez rendu le livre 'Le Petit Prince'.
Titre : Le Petit Prince, Auteur : Antoine de Saint-Exupéry, Nombre de pages : 96, Disponible : True
Le livre 'Le Petit Prince' est déjà disponible.
"""
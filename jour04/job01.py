# Class Personne
class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

# Class Eleve which inherits from Personne
class Eleve(Personne):
    def __init__(self, age=14):
        super().__init__(age)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

# Class Professeur
class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        # Private attribut
        self.__matiereEnseignee = matiereEnseignee  

    def enseigner(self):
        print("Le cours va commencer")

    def setMatiereEnseignee(self, matiere):
        self.__matiereEnseignee = matiere

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee


# Instantiation of the Person class and the Student class
personne = Personne()
eleve = Eleve()

# Displaying the default student age
eleve.afficherAge()

# Test
# Displaying the person's default age
personne.afficherAge()
# Changing the person's age and display it
personne.modifierAge(20)
personne.afficherAge()

# Display "Hello" for the personne
personne.bonjour()
# Displaying the default student age
eleve.afficherAge()
# Changing the person's age and display it
eleve.modifierAge(15)
eleve.afficherAge()
# Display "Hello"
eleve.bonjour()

# Instantiation of the Professeur class
professeur = Professeur()
# Displaying the default professor age
professeur.afficherAge()
# Changing the professor's age and display it
professeur.modifierAge(40)
professeur.afficherAge()
# Display "Hello"
professeur.bonjour()
# Display the default professor's subject
print(f"L'enseignant enseigne la matière {professeur.getMatiereEnseignee()}")
# Setting a new subject for the professor
professeur.setMatiereEnseignee("Mathématiques")
# Display the new professor's subject
print(f"L'enseignant enseigne la matière {professeur.getMatiereEnseignee()}")
# Display "Le cours va commencer" for the professor
professeur.enseigner()

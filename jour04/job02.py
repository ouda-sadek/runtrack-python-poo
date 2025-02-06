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


# Instantiation of the Student class
eleve = Eleve()

# Display "Hello"
eleve.bonjour()

# Display "Je vais en cours"
eleve.allerEnCours()

# Changing the person's age and display it
eleve.modifierAge(15)
eleve.afficherAge()


# Instantiation of the Professeur class
professeur = Professeur()

# Changing the professor's age and display it
professeur.modifierAge(40)
professeur.afficherAge()

# Display "Hello"
professeur.bonjour()

# Display "Le cours va commencer"
professeur.enseigner()


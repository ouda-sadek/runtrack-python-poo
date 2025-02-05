class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        # Private attributes
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        # Credits initialized to 0
        self.__credits = 0 
        # The student's level is calculated based on credits 
        self.__level = self.__student_eval() 
    """
    wWth the mutator method we change the credits but we cannot add them, hence the choice of the add method
    The mutator method allows us to change the student's level directly from the Student object itself
    # Mutator to directly define credits
    def set_credits(self, credits):
        if credits >= 0:
            self.__credits = credits
            # Update level after modification
            self.__level = self.__student_eval()  
        else:
            print("Erreur : Le nombre de crédits doit être supérieur ou égal à zéro.")
    """
    # Method for adding credits, with integrity verification
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            # We update the level after adding credits
            self.__level = self.__student_eval()  
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Private method to assess the student's level based on credits
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    # Method to display student information
    def student_info(self):
        print(f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits} points.")
        print(f"Nom : {self.__prenom}")
        print(f"Prénom : {self.__nom}")
        print(f"Id : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")

# Created  instance student John Doe
john_doe = Student("Doe", "John", 145)

# Adding credits
john_doe.add_credits(30)
john_doe.add_credits(50)
john_doe.add_credits(20)

# Display student information
john_doe.student_info()

# Creating class Personne()
class Personne:
    # The constructor which takes first and last name as parameters 
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    # Creating SePresenter method that returns the first and last name
    def SePresenter(self):
        return (f"Je suis {self.prenom} {self.nom}")

# Instantiating multiple Person objects
personne1 = Personne("Doe", "John")   
personne2 = Personne("Dupont", "Jean")
personne3 = Personne("Sadek", "Nass")

# Calling the SePresenter method for each person
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())

    


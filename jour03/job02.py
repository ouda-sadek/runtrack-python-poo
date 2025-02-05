class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    # Method to display account details
    def afficher(self):
        return (
            f"\nNuméro de compte : {self.__numero_compte}\n"
            f"Nom : {self.__nom}\n"
            f"Prénom : {self.__prenom}\n"
            f"Solde : {self.__solde}€\n"
            f"Droit au découvert : {'Oui' if self.__decouvert else 'Non'}\n"
        )

    # Method to display balance
    def afficherSolde(self):
        print(f"Solde du compte : {self.__solde}€\n")

    # Method for making a payment
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Erreur : Le montant du versement doit être positif.")

    # Method to make a withdrawal
    def retrait(self, montant):
        if montant > 0:
            if self.__solde - montant < 0 and not self.__decouvert:
                print("Erreur : Solde insuffisant, retrait non autorisé.")
            else:
                self.__solde -= montant
                print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Erreur : Le montant du retrait doit être positif.")

    # Method for applying fees
    def agios(self):
        if self.__solde < 0:
            # Agios of 5% of the negative balance
            agios_appliques = abs(self.__solde) * 0.05  
            self.__solde -= agios_appliques
            print(f"Agios de {agios_appliques}€ appliqués. Nouveau solde : {self.__solde}€")

    # Method for making a transfer to another account
    def virement(self, compte_bancaire, montant):
        if montant > 0:
            if self.__solde >= montant:
                self.__solde -= montant
                compte_bancaire.versement(montant)
                print(f"Virement de {montant}€ effectué vers le compte {compte_bancaire.__numero_compte}.")
            else:
                print("Erreur : Solde insuffisant pour effectuer le virement.")
        else:
            print("Erreur : Le montant du virement doit être positif.")

# Creating an account with example values
compte1 = CompteBancaire("123456789", "Dupont", "Pierre", 1000)
# Viewing account details
print(compte1.afficher())
# Displaying balances
compte1.afficherSolde()
# Testing payment and withdrawal methods
compte1.versement(500)  
compte1.retrait(200)    

# Creating an account with example values
compte2 = CompteBancaire("987654321", "Martin", "Lucie", -200, decouvert=True)
# Viewing account details
print(compte2.afficher())
# Displaying balances
compte2.afficherSolde()
# Testing payment and withdrawal methods
compte2.retrait(300)    
# Agios test
compte2.agios()

# Testing a transfer from account 1 to account 2
compte1.virement(compte2, 400)
# Displaying balances after transfer
compte1.afficherSolde()
compte2.afficherSolde()

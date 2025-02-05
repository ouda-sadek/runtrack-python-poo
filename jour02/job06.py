class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        # Dictionary of ordered dishes (name, price, status)
        self.__plats_commandes = {}
        # Order status, default "in progress"
        self.__statut = "en cours"

    # Assessors (getters)
    def get_num_commande(self):
        return self.__num_commande
    
    def get_plats_commandes__plats_commandes(self):
        return self.__plats_commandes
    
    def get_statut(self):
        return self.__statut
    
    # Mutators (setters)
    def set_statut(self, statut):
        if statut in ["en cours", "terminée", "annulée"]:
            self.__statut = statut
        else:
            print("Erreur : Le statut doit être 'en cours', 'terminée' ou 'annulée'.")

    # Method to add plat to commande
    def ajouter_plat(self, nom_plat, prix_plat, statut_plat="en préparation"):
        if self.__statut != "annulée":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": statut_plat}
        else:
            print("Erreur : Impossible d'ajouter un plat à une commande annulée.")

    # Method to cancel commande
    def annuler_commande(self):
        if self.__statut != "terminée":
            self.__statut = "annulée"
            print("La commande a été annulée.")
        else:
            print("Erreur : Impossible d'annuler une commande déjà terminée.")

    # Private method to calculate total of commande 
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    # Method to calculate VAT on the total (20% VAT)
    def calculer_TVA(self):
        total = self.__calculer_total()
        # 20%  TVA
        TVA = total * 0.20  
        return TVA
    
    # Method to display commande
    def afficher_commande(self):
        print(f"Commande n°{self.__num_commande}")
        print("Plats commandes :")
        for plat in self.__plats_commandes:
            print(f"- {plat.get_designation()} : {plat.get_prix()} ���")
        total, statut = self.calculer_total()
        print(f"Total : {total} ���")
        print(f"Statut : {statut}")
        print()

     # Method to display order information
    def afficher_commande(self):
        print(f"Numéro de commande : {self.__num_commande}")
        print(f"Statut de la commande : {self.__statut}")
        
        if self.__plats_commandes:
            print("Plats commandés :")
            for nom, details in self.__plats_commandes.items():
                print(f"  - {nom} : {details['prix']} EUR (Statut: {details['statut']})")
        else:
            print("Aucun plat commandé.")
        
        total = self.__calculer_total()
        tva = self.calculer_TVA()
        total_ttc = total + tva
        print(f"Total HT : {total} EUR")
        print(f"TVA (20%) : {tva} EUR")
        print(f"Total TTC : {total_ttc} EUR")

# Creating an order
commande1 = Commande(1234)

# Adding dishes orders to the order
commande1.ajouter_plat("Pizza Margherita", 12.50)
commande1.ajouter_plat("Spaghetti Bolognese", 15.00)

# Displaying order information before cancellation
commande1.afficher_commande()

# Cancel order
commande1.annuler_commande()

# Trying to add a dish to a canceled order
commande1.ajouter_plat("Salade César", 7.00)

# Show information again after cancellation
commande1.afficher_commande()

# Change order status to “completed”
commande1.set_statut("terminée")

# Trying to cancel an order that has already been completed
commande1.annuler_commande()   

#result
"""
Numéro de commande : 1234
Statut de la commande : en cours
Plats commandés :
  - Pizza Margherita : 12.5 EUR (Statut: en préparation)
  - Spaghetti Bolognese : 15.0 EUR (Statut: en préparation)
Total HT : 27.5 EUR
TVA (20%) : 5.5 EUR
Total TTC : 33.0 EUR
La commande a été annulée.
Erreur : Impossible d'ajouter un plat à une commande annulée.
Numéro de commande : 1234
Statut de la commande : annulée
Plats commandés :
  - Pizza Margherita : 12.5 EUR (Statut: en préparation)
  - Spaghetti Bolognese : 15.0 EUR (Statut: en préparation)
Total HT : 27.5 EUR
TVA (20%) : 5.5 EUR
Total TTC : 33.0 EUR
Erreur : Impossible d'annuler une commande déjà terminée.
"""

# Create class 
class Produit:
    # Initialize the product attributes
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        
    # Method to apply TVA
    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA/100)

    # Method to display the product information
    def afficher(self):
        print(f"Produit: {self.nom}")
        print(f"Prix HT: {self.prixHT}€")
        print(f"TVA: {self.TVA}%")
        print(f"Prix TTC: {self.calculerPrixTTC()}€\n")

    
    # Method to calculate the product's price after applying TVA
    def prixTTC(self):
        return self.prixHT * (1 + self.TVA/100)
    
    # Method to change the product name
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    # Method to change the product price
    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    
    # Method to calculate the discounted price after applying a given discount
    def prixAvecRemise(self, pourcentageRemise):
        return self.prixTTC() * (1 - pourcentageRemise/100)
    
    # Methods for returning product information
    def getNom(self):
        return self.nom
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA
    
    def getPrixTTC(self):
        return self.calculerPrixTTC()
    
# Creation of several products
produit1 = Produit("Ordinateur", 3500, 20)
produit2 = Produit("Smartphone", 1200, 20)
produit3 = Produit("Tablette", 950, 20)

# Displaying initial information
produit1.afficher()
produit2.afficher()
produit3.afficher()

# Editing product information
produit1.modifierNom("Ordinateur portable")
produit1.modifierPrix(1200)

produit2.modifierNom("Smartphone 5G")
produit2.modifierPrix(900)

produit3.modifierNom("Tablette Pro")
produit3.modifierPrix(650)

# Displaying information after modification
produit1.afficher()
produit2.afficher()
produit3.afficher()

# Results
"""Produit: Ordinateur
Prix HT: 3500€
TVA: 20%
Prix TTC: 4200.0€

Produit: Smartphone
Prix HT: 1200€
TVA: 20%
Prix TTC: 1440.0€

Produit: Tablette
Prix HT: 950€
TVA: 20%
Prix TTC: 1140.0€

Produit: Ordinateur portable
Prix HT: 1200€
TVA: 20%
Prix TTC: 1440.0€

Produit: Smartphone 5G
Prix HT: 900€
TVA: 20%
Prix TTC: 1080.0€

Produit: Tablette Pro
Prix HT: 650€
TVA: 20%
Prix TTC: 780.0€"""

    



    

   

   


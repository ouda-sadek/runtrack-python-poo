class Produit:
    # Initialize the product attributes
    def __init__(self, nom, prixHT, TVA):
        self.__nom = nom
        self.__prixHT = prixHT
        self.__TVA = TVA
        
    # Method to apply TVA
    def calculerPrixTTC(self):
        return self.__prixHT * (1 + self.__TVA / 100)

    # Method to return the product information as a string
    def afficher(self):
        return (
            f"Produit: {self.__nom}\n"
            f"Prix HT: {self.__prixHT}€\n"
            f"TVA: {self.__TVA}%\n"
            f"Prix TTC: {self.calculerPrixTTC()}€\n"
        )
    
    # Method to calculate the product's price after applying TVA
    def prixTTC(self):
        return self.__prixHT * (1 + self.__TVA / 100)
    
    # Method to change the product name
    def modifierNom(self, nouveau_nom):
        self.__nom = nouveau_nom

    # Method to change the product price
    def modifierPrix(self, nouveau_prix):
        self.__prixHT = nouveau_prix

    # Method to calculate the discounted price after applying a given discount
    def prixAvecRemise(self, pourcentageRemise):
        return self.prixTTC() * (1 - pourcentageRemise / 100)
    
    # Methods for returning product information
    def getNom(self):
        return self.__nom
    
    def getPrixHT(self):
        return self.__prixHT
    
    def getTVA(self):
        return self.__TVA
    
    def getPrixTTC(self):
        return self.calculerPrixTTC()


# Creation of several products
produit1 = Produit("Ordinateur", 3500, 20)
produit2 = Produit("Smartphone", 1200, 20)
produit3 = Produit("Tablette", 950, 20)

# Displaying initial information by calling the 'afficher' method and using print()
info_produit1 = produit1.afficher()
info_produit2 = produit2.afficher()
info_produit3 = produit3.afficher()

# Editing product information
produit1.modifierNom("Ordinateur portable")
produit1.modifierPrix(1200)

produit2.modifierNom("Smartphone 5G")
produit2.modifierPrix(900)

produit3.modifierNom("Tablette Pro")
produit3.modifierPrix(650)

# Displaying information after modification by calling the 'afficher' method and using print()
nouveau_info_produit1 = produit1.afficher()
nouveau_info_produit2 = produit2.afficher()
nouveau_info_produit3 = produit3.afficher()

# Results
# To display these results, you will use print() outside the class:
print(info_produit1)
print(info_produit2)
print(info_produit3)

print(nouveau_info_produit1)
print(nouveau_info_produit2)
print(nouveau_info_produit3)

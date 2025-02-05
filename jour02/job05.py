class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        # Car off by default
        self.__en_marche = False
        # The tank is initialized to 50 liters by default
        self.__reservoir = 50

    # Assessors (getters) for each attribute
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    def get_reservoir(self):
        return self.__reservoir
    
    # Mutators (setters) for each attribute
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        # Ensure that the tank is not negative
        if reservoir >= 0:  
            self.__reservoir = reservoir
        else:
            print("Erreur : Le réservoir ne peut pas avoir une valeur négative.")

    # Private method to check fuel level
    def __verifier_plein(self):
        return self.__reservoir
    
    # Method for starting the car
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer : réservoir insuffisant (moins de 5 litres).")

    # Method to stop the car
    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    # Method to display car information
    def afficher_info(self):
        print(f"Marque : {self.__marque}")
        print(f"Modèle : {self.__modele}")
        print(f"Année : {self.__annee}")
        print(f"Kilométrage : {self.__kilometrage} km")
        print(f"En marche : {'Oui' if self.__en_marche else 'Non'}")
        print(f"Réservoir : {self.__reservoir} litres")

# Creating an instance of the car
ma_voiture = Voiture("Toyota", "Corolla", 2020, 15000)

# Displaying information before starting
ma_voiture.afficher_info()

# Attempting to start the car (full tank)
ma_voiture.demarrer()

# Add fuel (4 liter tank)
ma_voiture.set_reservoir(4)

# Attempting to start the car with insufficient fuel
ma_voiture.demarrer()

# Start the car with enough fuel
ma_voiture.set_reservoir(10)
ma_voiture.demarrer()

# Stop the car
ma_voiture.arreter()

# Displaying information after stopping the car
ma_voiture.afficher_info()

#result
"""
Marque : Toyota
Modèle : Corolla
Année : 2020
Kilométrage : 15000 km
En marche : Non
Réservoir : 50 litres
La voiture a démarré.
Impossible de démarrer : réservoir insuffisant (moins de 5 litres).
La voiture a démarré.
La voiture est arrêtée.
Marque : Toyota
Modèle : Corolla
Année : 2020
Kilométrage : 15000 km
En marche : Non
Réservoir : 10 litres
"""

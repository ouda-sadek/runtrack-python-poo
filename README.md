# runtrack-python-poo

JOUR01:
    JOB01 + JOB02:
# method to display the object in a readable way
        def __repr__(self):
        return f"Operation(nombre1={self.nombre1}, nombre2={self.nombre2})"
# Result
        Operation(nombre1=0, nombre2=0)

    JOB03:
# Creating addition() method 
        def addition(self):
        return self.nombre1 + self.nombre2
# Creating the instance of the class with specific values
    operation = Operation(12, 3)
# Displaying the object in the console
    print(f"Le resultat est {Operation.addition(operation)}")

    JOB08:
# calculating the perimetre.....
        we ca use math.pi to calculate the perimetre value .....
        but we have to import math
        
# JOUR02 / job06
results   
Numéro de commande : 1234
Statut de la commande : en cours
plats_commandes__plats_commandes commandés :
  - Pizza Margherita : 12.5 EUR (Statut: en préparation)
  - Spaghetti Bolognese : 15.0 EUR (Statut: en préparation)
Total HT : 27.5 EUR
TVA (20%) : 5.5 EUR
Total TTC : 33.0 EUR
La commande a été annulée.
Erreur : Impossible d'ajouter un plat à une commande annulée.
Numéro de commande : 1234
Statut de la commande : annulée
plats_commandes__plats_commandes commandés :
  - Pizza Margherita : 12.5 EUR (Statut: en préparation)
  - Spaghetti Bolognese : 15.0 EUR (Statut: en préparation)
Total HT : 27.5 EUR
TVA (20%) : 5.5 EUR
Total TTC : 33.0 EUR
Erreur : Impossible d'annuler une commande déjà terminée.
rs_5@MacBook-Pro-de-Rayanne jour02 % /opt/homebrew/bin/python3 /Users/rs_5/Desktop/laplateforme/IA/Runtrack_python_poo/runtrack-python-poo/jour02/job06.py
Numéro de commande : 1234
Statut de la commande : en cours
plats_commandes__plats_commandes commandés :
  - Pizza Margherita : 12.5 EUR (Statut: en préparation)
  - Spaghetti Bolognese : 15.0 EUR (Statut: en préparation)
Total HT : 27.5 EUR
TVA (20%) : 5.5 EUR
Total TTC : 33.0 EUR
La commande a été annulée.
Erreur : Impossible d'ajouter un plat à une commande annulée.
Numéro de commande : 1234
Statut de la commande : annulée
plats_commandes__plats_commandes commandés :
  - Pizza Margherita : 12.5 EUR (Statut: en préparation)
  - Spaghetti Bolognese : 15.0 EUR (Statut: en préparation)
Total HT : 27.5 EUR
TVA (20%) : 5.5 EUR
Total TTC : 33.0 EUR
Erreur : Impossible d'annuler une commande déjà terminée.

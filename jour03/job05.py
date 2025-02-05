import random

# Definition of the Character class
class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        """Method to attack the opponent and inflict damage."""
        # Random damage between 10 and 20
        degats = random.randint(10, 20)  
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

    def est_vivant(self):
        """Checks if the character is still alive (life > 0)."""
        return self.vie > 0

    def afficher_vie(self):
        """Shows the character's current life."""
        print(f"{self.nom} a {self.vie} points de vie.")

# Definition of the Game class
class Jeu:
    def __init__(self):
        # Default level
        self.niveau = 1  
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        """Asks the player to choose the difficulty level."""
        while True:
            try:
                self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))
                if self.niveau not in [1, 2, 3]:
                    raise ValueError("Le niveau doit être 1, 2 ou 3.")
                break
            except ValueError as e:
                print(e)

    def lancerJeu(self):
        """Launch the game according to the chosen level."""
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 80
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 120
        else:
            vie_joueur = 60
            vie_ennemi = 150
        
        # Creation of characters
        self.joueur = Personnage("Joueur", vie_joueur)
        self.ennemi = Personnage("Ennemi", vie_ennemi)

        # Start the fight
        self.combattre()

    def combattre(self):
        """Method for managing the progress of combat."""
        tour = 1
        while self.joueur.est_vivant() and self.ennemi.est_vivant():
            print(f"\nTour {tour} :")
            # Displaying character lives
            self.joueur.afficher_vie()
            self.ennemi.afficher_vie()
            
            # The player attacks
            self.joueur.attaquer(self.ennemi)
            if not self.ennemi.est_vivant():
                print("\nL'ennemi est vaincu ! Vous avez gagné !")
                break

            # The enemy attacks
            self.ennemi.attaquer(self.joueur)
            if not self.joueur.est_vivant():
                print("\nVous êtes vaincu ! L'ennemi a gagné.")
                break
            
            tour += 1

# Creating the Game object and starting the game
jeu = Jeu()
# Ask the player to choose a level
jeu.choisirNiveau() 
# Start the game with the characters
jeu.lancerJeu()  
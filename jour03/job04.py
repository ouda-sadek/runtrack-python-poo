# Class Joueur
class Joueur:
    def __init__(self, nom, numero, position):
        # Initializing attributes
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    # Methods to update player statistics
    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    # Method to display player statistics
    def afficherStatistiques(self):
        return (f"Nom: {self.nom}\n"
                f"Numéro: {self.numero}\n"
                f"Position: {self.position}\n"
                f"Buts: {self.buts}\n"
                f"Passes Décisives: {self.passes_decisives}\n"
                f"Cartons Jaunes: {self.cartons_jaunes}\n"
                f"Cartons Rouges: {self.cartons_rouges}\n")

# Class Equipe
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    # Method to add a player to the team
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    # Method to display statistics of all players in the team
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom} :\n")
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())
            print("-" * 30)

    # Method to update stats for a specific player
    def mettreAJourStatistiquesJoueur(self, joueur, action):
        if action == "but":
            joueur.marquerUnBut()
        elif action == "passe":
            joueur.effectuerUnePasseDecisive()
        elif action == "carton_jaune":
            joueur.recevoirUnCartonJaune()
        elif action == "carton_rouge":
            joueur.recevoirUnCartonRouge()

# Creating player
joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Sergio Ramos", 4, "Défenseur")
joueur3 = Joueur("Kylian Mbappé", 7, "Attaquant")
joueur4 = Joueur("Neymar Jr", 11, "Attaquant")

# Creating a team
equipe1 = Equipe("Paris Saint-Germain")

# Add players to the team
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)

# Viewing team stats before a match
equipe1.afficherStatistiquesJoueurs()

# Simulation of a match
equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur2, "carton_jaune")
equipe1.mettreAJourStatistiquesJoueur(joueur3, "passe")
equipe1.mettreAJourStatistiquesJoueur(joueur4, "carton_rouge")

# Viewing statistics after the match
print("\nStatistiques après le match :")
equipe1.afficherStatistiquesJoueurs()

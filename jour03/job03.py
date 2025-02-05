class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        # Default status: “to do”
        self.statut = statut  
    
    # Method to mark task as completed
    def marquerCommeFinie(self):
        self.statut = "terminée"

    # Viewing the task
    def __str__(self):
        return f"Titre: {self.titre}\nDescription: {self.description}\nStatut: {self.statut}\n"

class ListeDeTaches:
    def __init__(self):
        # Empty task list
        self.taches = []  
    
    # Method to add a task to the list
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    # Method to delete a task
    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
        else:
            print(f"Tâche '{tache.titre}' non trouvée dans la liste.")
    
    # Method to mark a task as completed
    def marquerCommeFinie(self, tache):
        if tache in self.taches:
            tache.marquerCommeFinie()
        else:
            print(f"Tâche '{tache.titre}' non trouvée dans la liste.")
    
    # Method to display all tasks
    def afficherListe(self):
        if self.taches:
            for tache in self.taches:
                print()
        else:
            print("Aucune tâche à afficher.")
    
    # Method to filter tasks by status
    def filterListe(self, statut):
        filtered_taches = [tache for tache in self.taches if tache.statut == statut]
        return filtered_taches

# Creating the task list
liste = ListeDeTaches()

# Creating multiple tasks
tache1 = Tache("Faire les courses", "Acheter des légumes et des fruits.")
tache2 = Tache("Étudier Python", "Revoir les concepts de classes et objets.")
tache3 = Tache("Aller à la salle de sport", "Séance de 1h de musculation.")

# Add tasks to list
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# Show all tasks
print("Liste des tâches :")
liste.afficherListe()

# Mark the “Study Python” task as completed
liste.marquerCommeFinie(tache2)

# View tasks after editing
print("\nListe des tâches après modification :")
liste.afficherListe()

# Filter “to do” tasks
taches_a_faire = liste.filterListe("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)

# Delete the “Shopping” task
liste.supprimerTache(tache1)

# Show list after deletion
print("\nListe des tâches après suppression :")
liste.afficherListe()

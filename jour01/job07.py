# create class Personnage
class Personnage:
    # Character position initialization
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to move the character to the left
    def gauche(self):
        self.x -= 1

    # Method to move the character to the right
    def droite(self):
        self.x += 1

    # Method to move the character upwards
    def haut(self):
        self.y -= 1

    # Method to move the character downwards                                            
    def bas(self):
        self.y += 1

    # Method to get the character's current position
    def position(self):
        return (self.x, self.y)
    
if __name__ == "__main__":

    # Creation of a character at position (2, 3) on the board
    personnage = Personnage(2, 3)
    
    # Display initial position 
    print("Position initiale :", personnage.position())  
    
    # Character movement
    personnage.gauche()
    print("Après déplacement à gauche :", personnage.position())  
    
    personnage.droite()
    print("Après déplacement à droite :", personnage.position())  
    
    personnage.bas()
    print("Après déplacement vers le bas :", personnage.position())  
    
    personnage.haut()
    print("Après déplacement vers le haut :", personnage.position()) 

    personnage.position() 
    print("Position du personnage : ", personnage.position()) 
        

    #results 
    # Position initiale : (2, 3)
    # Après déplacement à gauche : (1, 3)
    # Après déplacement à droite : (2, 3)
    # Après déplacement vers le bas : (2, 4)
    # Après déplacement vers le haut : (2, 3)
    # Position du personnage :  (2, 3)
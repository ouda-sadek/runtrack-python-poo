# Create class Circle
class Cercle:
    # Initialize the radius of the circle
    def __init__(self, rayon):
        self.rayon = rayon

    # Create a method that change the radius of the circle
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    # Create a method that display all the information about the circle
    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

    # Create a method that return circumference of a circle
    def circonference (self):
        return 2 * 3,14 * self.rayon
        
    # Create a method that return surface of a circle
    def aire(self):
        return 3,14 * (self.rayon ** 2)
    
    # Create a method that return perimeter of a circle
    def diametre(self):
        return 2 * self.rayon
    
if __name__ == "__main__":
    # Create a circle with radius= 5 
    cercle = Cercle(4)
    
    # display the all informarions after the change of radius
    cercle.afficherInfos()
    
    # Change the radius to 10
    cercle.changerRayon(7)
    
    # Display information after the change is done 
    print("\nAprès modification du rayon:") 
    cercle.afficherInfos()


    #results
    # Rayon : 4
    # Diamètre : 8
    # Circonférence :  (6, 56)               50.26548245743669 
    # Aire :  (3, 224)              50.26548245743669
    # 
    # Après modification du rayon:
    # Rayon : 7
    # Diamètre : 14
    # Circonférence :  (6, 98)            (14, 87.96459430051493)     251.32741228718345
    # Aire :  (3, 686)              157.07963267948966
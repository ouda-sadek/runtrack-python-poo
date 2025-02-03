# Creating class Point
class Point:
    # The constructor (__init__) initializes the "x" and "y" attributes with default values
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Method to display the coordinates of the point1
    def afficherLesPoints(self):
        print(f"Les coordonnées du point1 sont ({self.x}, {self.y})")

    # Method to display x
    def afficherX(self):
        print(f"L'abscisse du point1 est {self.x}")

    # Method to display y
    def afficherY(self):
        print(f"L'ordonnée du point1 est {self.y}")

    # Method to change x
    def changerX(self, new_x):
        self.x = new_x

    # Method to change y
    def changerY(self, new_y):
        self.y = new_y

# Creating a Point object
point1 = Point()
point2 = Point(1, 5)

# Displaying the coordinates of the point1
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()

point2.afficherLesPoints()
point2.afficherX()
point2.afficherY()

# Changing the x and y coordinates of point1
point1.changerX(5)
point1.changerY(4)

# Displaying the new coordinates of the point1
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
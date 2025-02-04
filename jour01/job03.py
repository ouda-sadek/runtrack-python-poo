# Creating class Operation()
class Operation:
    # The constructor (__init__) initializes the "number1" and "number2" attributes with default values
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # Method to add number1 and number2 and display the result
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le resultat est {resultat}")

# Creating the instance of the class with specific values
operation = Operation(12, 3)

# Calling the addition method to display the result
operation.addition()





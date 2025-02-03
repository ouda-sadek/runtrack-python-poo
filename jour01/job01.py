class Operation:
    # The constructor (__init__) initializes the 'number1' and 'number2' attributes with default values
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Creating the instance of the class with default values
operation = Operation()

# Displaying the object in the console
print(operation)
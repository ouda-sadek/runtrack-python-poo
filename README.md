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
        
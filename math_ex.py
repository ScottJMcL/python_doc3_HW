import math

def house():
    '''
        Calculates the square footage of a house. Inputs must be numbers.
        Formula: Length X Width == Area
    '''
    length = float(input("Enter length of the house: "))
    width = float(input("Enter width of the house: "))
    try:
        area = length * width
        return area
        
    except:
        print("Inputs MUST be numbers.")

    

def cricumference():
    '''
        Calculates the circumference of a circle. Input must be a number, and 
        should be the Radius (Diameter / 2).
    '''
    radius = float(input("Enter the radius (D/2): "))
    try:
        circ = math.pi * (radius ** 2)
        circ = round(circ, 4)
        return circ
    except:
        print("Input MUST be a number.")

print(f"\nThe house is {house()} sq ft")

print(f'\nCircumference is {cricumference()}\n')

import math
import sys;

def Calc_Area(r):
    """help"""
    area = math.pi * r**2
    return area

#Cálculo del área del círculo
radius = 5 
Area = Calc_Area(radius)
print("Area of circle: ", Area)

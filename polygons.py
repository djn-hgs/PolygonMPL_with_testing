import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
 
 
class Coord:
    def __init__(self, x1, y1):
        self.point = np.array((x1, y1))
 
    def distance(self, other):
        pass
 
 
class Polygon:
    def __init__(self, *args):
        self.points = np.array([point for point in args])
 
    def perimeter(self):
        pass
 
    def plot(self):
        pass
 
 
class Triangle(Polygon):
    def __init__(self, p0, p1, p2):
        pass
 
    def area(self):
        pass

# Complete the .distance method of Coord to find the Cartesian distance between 2 Coords
#	Install pytest and write a test function to create two points and check that the distance between them is correct.
#	Write the .perimeter method of the Polygon by summing the cartesian distances between successive points.
#	Again write a test function to test the distance.
#	Complete the __init_ method for the Triangle subclass by calling the super() command.
#	Write a .area method for the Triangle class that will calculate the area using Heron’s formula.

import math

def circumference(radius):
    return 2 * math.pi * radius

r = float(input("Enter the radius: "))

print("Circumference =", circumference(r))
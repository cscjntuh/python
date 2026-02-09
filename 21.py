import math

def area_circle(r):
    return math.pi * r * r

r = float(input("Enter radius: "))
print("Area of circle:", area_circle(r))

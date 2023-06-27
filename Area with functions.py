from math import pi

def areaofcircle(radius):
    return pi * radius * radius

def main():
    r = float(input("Enter the radius: "))
    print("The area of the circle is", areaofcircle(r))

main()

from math import pi
radius = float(input('Enter the radius: '))
if radius <= 0:
    print('ERROR: Input number must be a positive number')
else:
    area = pi * radius ** 2
print('The area of the circle is', area) 

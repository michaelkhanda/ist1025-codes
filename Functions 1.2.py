from math import sqrt

def square (x):
    return x * x

def hypotenuse(x,y):
    return sqrt (square(x) + square(y))


a = float(input("Enter a number to square: "))

print("The square is", square(a))

b = float(input("Enter another number: "))

print("The length of the hypotenuse of a", a, "by",
      b, "right angle triangle is", hypotenuse(a,b))

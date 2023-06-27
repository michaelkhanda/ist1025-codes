number = int(input("Enter a number between 0 and 100: "))

if number < 0:
    number = -number
if number > 100:
    number = 100

print(number)

number = (input("Enter a number between 0 and 100: "))


if  number.isdigit()or "-" in number:
    number = int(number)
if number < 0:
    number = -number
if number > 100:
    number = 100
    print(number)

else:
    print("ERROR: You entered a letter or letters")

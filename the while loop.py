from math import sqrt

x = float(input('Enter a number: '))
count = int(input('Enter the number of iterations: '))

guess = x/2
i = 0
while i < count:
            guess = (guess + x/guess)/2
            i =  i + 1
print(f'Guess: {guess: 0.15f}')
print(f'actual: {sqrt(x): .15f}')

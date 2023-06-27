from math import sqrt

x = float(input('Enter a number: '))
count = int(input('Enter the number of iterations: '))

guess = x/2
for i in range(count):
            guess = (guess + x/guess)/2
print(f'Guess: (guess: 0.15f)')

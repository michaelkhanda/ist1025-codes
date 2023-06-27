from math import sqrt

x = float(input('Enter a number: '))

tolerance = 0.00001
guess = x/2

count = 0
while abs(guess * guess - x) > tolerance:
            guess = (guess + x/guess)/2
            count = count + 1
            
print(f'Guess: {guess: 0.15f}')
print(f'actual: {sqrt(x): .15f}')
print('Number of iterations is', count)

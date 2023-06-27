rate = int(input('Enter the interest rate[0-100]: '))
if rate < 0:
    print('ERROR: Rte must be greater than 0!')
elif rate >100:
    print('ERROR: Rate must be less than 101!')
else:
    principal = 1000
    interest = principal * rate/100
    print('Your interest is', interest)

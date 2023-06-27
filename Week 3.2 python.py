principal = 10000
rate = 0.06
term = 5
totalinterest = 0
print('YEAR AMOUNT INTEREST')
for year in range(term):
    interest = principal * rate
##    print(year, round(principal, 2), round(interest, 2))
    print(f'{year} {principal: .2f} {interest: .2f}')
    principal = principal + interest
    totalinterest = totalinterest + interest
##    print('Total Interest: ', round(totalinterest, 2))
    print(f'{Total Interest: {totalinterest: .2f}')
##    print('Total Principal: ', round(principal, 2))
    print(f'{Total Principal: {principal: .2f'})

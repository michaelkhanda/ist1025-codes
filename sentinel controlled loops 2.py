total = 0
count = 0
data = float(input('Enter a score or -9 to quit: '))

while data != -9:
    count += 1
    total += data
    data = float(input('Enter a score or just return to quit: '))

if count == 0:
    print('No scores were entered. ')
else:
    print('The avaerage is', total/count)

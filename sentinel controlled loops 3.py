total = 0
count = 0


while True :
    data = input('Enter a score or just return to quit: ')
    if data == '':
            break
    total += int(data)
    count += 1

if count == 0:
    print('No scores were entered. ')
else:
    print('The avaerage is', total/count)

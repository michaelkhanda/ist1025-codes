filename = input('Enter the file name: ')
f = open(filename, 'r')

for line in f:
    print(line)
    

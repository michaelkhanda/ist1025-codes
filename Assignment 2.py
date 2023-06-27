#PART ONE OF THE QUESTION#

def getAverage(filename):
    return total + int(filename)

file = open("numbers.txt", "r")
f = file.readlines()
total = 0
for line in f:
    for filename in line:
        if filename.isdigit():
            total = total + int(filename)

print("The sum of the numbers is:", total)



            

#PART TWO OF THE QUESTION#
def getAverage(filename):
    return total/4

def main():
    filename = input("Enter a file name: ")
    myfile = open(filename, "r")
    print ("The average of the numbers is:", getAverage(filename))
    

if __name__ == "__main__":
    main()

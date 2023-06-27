scorelist = []
score = float(input("Enter a score or -1 to quit: "))
scorelist.append(score)

while score != -1:
    score = float(input("Enter a score or -1 to quit: "))
    scorelist.append(score)
    count = count + 1

print("You have", count-1, "scores.")
    

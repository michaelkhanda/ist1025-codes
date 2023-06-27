shopping = ["oranges", 5, "Apples", 7, "Milk", 2, "Bread", 1]

"""
when i is 0 print item in i + 1 (1) followed by item in i (0)
when i is 1 skip
when i is 2 print item in i + 1 (3) followed by item in i (2)

"""

for i in range(len(shopping)):
    if i % 2 == 0:
        print(shopping[i + 1], shopping[i])

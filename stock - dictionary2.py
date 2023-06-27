stock = {}

while True:
    item = input("Enter an item or just press Enter to quit: ")
    if item == "":
        break
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    stock[item] = [price, quantity]

print(stock)

total = 0
for item in stock:
    total = total + stock[item][0] * stock[item][1]
print("Your stock is worth", total)


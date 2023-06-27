item = input("Enter an item or just press Enter to quit: ")

stock = {}
while item != "":
    price = float(input("Enter the price: "))
    stock [item] = price
    item = input("Enter an item or just press Enter to quit: ")

print(stock)

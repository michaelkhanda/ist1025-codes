message = input("Enter your message: ")

code = ""
for ch in message:
    code = code + str(ord(ch)) + " "

print ("Here is your encrypted message.")

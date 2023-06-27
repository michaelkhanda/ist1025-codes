message = input("Enter your message: ")


#Encrypt
code = ""
for ch in message:
    code = code + str(ord(ch)) + " "

print ("Here is your encrypted message.")


#decrypt
original = ''
for number in code.split():
    original = original + chr(int(number))
    

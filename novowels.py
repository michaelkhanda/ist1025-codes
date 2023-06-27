greeting = "Hello, how are you today"
nv=''
for ch in greeting:
    if ch not in "aeiouAEIOU":
        nv = nv + ch
print(nv)

sentence = input("Enter a sentence: ")
nv = ""
x = "aeiouAEIOU"
for ch in sentence:
    if ch not in "x":
        nv = nv + ch
print(nv)

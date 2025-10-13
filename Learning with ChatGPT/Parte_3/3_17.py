#write functiont that change lower char to capital and viceversa
low = "abcdefghijklmnopqrstuvxyz"
upp = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
def invert_case(text):
    reversedchar = ""
    reversedtext = ""
    for char in text:
        if char in low:
            reversedchar = char.capitalize()
            reversedtext = reversedtext + reversedchar 
        elif char in upp:
            reversedchar = char.lower()
            reversedtext = reversedtext + reversedchar
    return reversedtext
text = input("Insert text : ")
print(invert_case(text))
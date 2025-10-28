#write functiont that count numbers letters and signs inside text
#num = "1234567890"                              #Daniel1992!
#let = "abcdefghijklmnopqrstuvxyz"
#sig = ",.<>/;:~!@%^&*_-+= "
def analyze_text(text):
    numc = 0
    letc = 0
    sigc = 0
    if text == "":
        return ("Text wasn't inserted")
    else:
        for char in text:
            #if char in num:
            if char.isdigit():
                numc += 1
            #if char in let:
            if char.isalpha():
                letc += 1
            #if char in sig:
            else:
                sigc += 1
        #return ("Numbers = ", numc, "Letters = ", letc, "Signs = ", sigc)
        return f"Numbers:  {numc}, Letters: {letc}, Signs: {sigc}"
text = input("Insert text : ").lower()
print(analyze_text(text))
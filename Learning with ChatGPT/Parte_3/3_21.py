#write function that censor word in text
def censor(text, word):
    return text.replace(word,"*" * len(word))   
text = input("Insert text : ")
word = input("Insert word to censor : ")
print(censor(text, word))
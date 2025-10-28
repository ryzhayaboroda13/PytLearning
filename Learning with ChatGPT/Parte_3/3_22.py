#write function that count word in text
def word_counter(text):
    count = 0
    if text == "":
            return f"Insert text please"
    for char in text:  
        if  char == ' ': count += 1
    count += 1
    return f"Word in text = {count}"
        
text = input("Insert text : ")
print(word_counter(text))
#write function that count how may times characters repeats in text
vocab = "abcdefghijklmnopqrstuvxyz"
def char_frequency(text):
    count = 0
    tot = 0
    for char in vocab:
        for i in range(0, len(text)):
            if char == text[i].lower():
                count += 1
                tot += 1
        if count > 0:
            print(char, count)
            count = 0
            if tot == len(text):
                break   
text = input("Insert text : ")
print(char_frequency(text))
#write function that delete every vowels in text
vowels = "aeiouAEIOU"
def delete_vowels(text):
    text_no_vowels = ""
    for char in text:
        if char not in vowels:
            text_no_vowels = text_no_vowels + char
    return text_no_vowels
text = input("Insert text : ")
print(delete_vowels(text))
#write function that check if word is palindrome
def is_palindrome(text):
    for char in text:
        for i in range(len(text), 0):
            if char != text[i].lower():
                print(text, "is not palindrome")
            else:
                print(text, "is palindrome")
text = input("Insert text : ")
print(is_palindrome(text))
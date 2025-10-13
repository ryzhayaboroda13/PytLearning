#write function that check if word is palindrome
def is_palindrome(text):
    if text == text[::-1]:
        print(text, " is palindrome")
    else:
        print(text, " is not palindrome")
        
text = input("Insert text : ").lower().replace(" ","")
print(is_palindrome(text))
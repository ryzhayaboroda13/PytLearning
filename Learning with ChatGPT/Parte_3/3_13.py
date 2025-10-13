#write function that count glassnye and soglassnye
def count_letters(text):
    glassnye = "aeiou"
    soglassnye = "bcdfghjklmnpqrstvxyz"
    glassnye_count = 0
    soglassnye_count = 0
    for char in text:
        if char in glassnye:
            glassnye_count += 1
        elif char.isalpha():
            soglassnye_count += 1
    return (glassnye_count,soglassnye_count)

text = input("Insert your text ").replace(" ","")
print(count_letters(text))
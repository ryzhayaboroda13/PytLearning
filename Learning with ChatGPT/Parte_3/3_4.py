#scrivi una funzione che fa il riverso. Esempio Ciao -> oaiC
def reverse_text(txt):
    reversed_str = ""
    for char in txt:
        reversed_str = char + reversed_str
    return  reversed_str
txt = input("Inserisci il testo da capovolgere: ")
print(reverse_text(txt))
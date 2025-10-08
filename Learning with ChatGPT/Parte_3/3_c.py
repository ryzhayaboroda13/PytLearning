#scrivi una funzione che controlla se il numero e` pari o dispari
def dispar(a):
    n = a % 2
    if n == 0:
        return f"{a} e` pari"
    else:
        return f"{a} e` dispari"

a = int(input("Inserisci il numero da verificare: "))
print(dispar(a))
#scrivi una funzione che trova il numero piu` grande tra quelli inseriti
def find_max():
    numbers=[]
    while True:
        user_input = input("Insersci in numero da confrontare(stop - per fermare): ")
        if user_input.lower() == 'stop':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Inserisci un numero o 'stop'.")
    if numbers:
            max_number = max(numbers)
            print(f"Numeri insertiti {numbers}")
            print(f"Il numero piu` grande e` {max_number}")
            return max_number
    else:
            print("Numeri non sono stati inseriti")
            return None      


find_max()
#Esercizio 2.1.c
database = ["ivan", "maria", "petr"]
name = input("Come ti chiami? ").strip()            #убираем лишние пробелы
if name.lower() in database:
    print(f"Ciao, {name}")
else:
    print("Ciao sconosciuto")

#1.1 come creare una funzione
#esempio
def greet(name):
    #def    - parola chiave per dichiarare la funzione
    #greet  - nome della funzione
    #name   - parametro della funzione, che memorizza il valore assegnato alla funzione
    #QUA SOTTO si trova il corpo della funzione dove all'interno verrano scritte istruzioni da eseguire
    #in questo caso visualizziamo il nome
    print(f"Ciao, {name}!")

#richiamo della funzione
greet("Ivan")                   #all'interno delle parentesi assegnamo alla variabile name il nome "Ivan"

#------------------------------------------
#1.2 funzioni con il ritorno del risultato
def add(a,b):
    #questa e` una funzione con due parametri, a e b
    return a + b
    #la funzione esegue la somma di due variabili a e b

#richiamo della funzione
result = add(3, 4)              #alla variabile result viene assegnata la somma di due numeri tramite la funzione add
print(result)

#------------------------------------------
#1.3 moduli in python
#moduli - fuonzioni gia` predefinite in python
#Come si fa a richiamare un modulo
import math                     #math - modulo con funzioni matematiche
print(math.sqrt(16))            #sqrt - radice di un numero

#Come si fa a creare un modulo(funzione da un file esterno)
import  my_module
print(my_module.greet("Ivan"))  
#in questo modo abbiamo richiamato la funzione 'greet' dal modulo 'my_module'

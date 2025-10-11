#scrivi un modulo che contiene la funzione per calcolare l'area di un cerchio 
#pi * r^2
def areacerchio(r):
    area = 3.14 * r * r
    return area


#scrivi una funzione che controlla se il numero e' primo
def is_prime(num):
    if num < 1:
        return "Number isn't prime"
    
    for i in range(2, num):
        if num % i == 0:
            return "Number isn't prime"
        
    return "Number is prime"
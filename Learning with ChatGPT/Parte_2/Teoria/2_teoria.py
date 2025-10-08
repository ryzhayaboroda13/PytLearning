#variabili
age = 25                                        #variabile integer
name = "Ivan"                                   #variabile string
height = 1.85                                   #variabile float
is_student = True                               #variabile boolean

#operazioni matematiche
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#incatenamento dell righe
greeting = "Ciao, " + name      
print (greeting)
print('Ciao,', name)                            #stessa cosa di prima

#condizioni
age = 18
if age >= 18:
    print("Sei gia` grande!")                   #""
else:
    print('Sei ancora troppo piccolo.')         #''

#ciclo FOR
for i in range(5):                              #nel range 5 ---> da 0 a 4
    print(i)

#ciclo WHILE
count = 0
while count < 5:
    print(count)
    count += 1

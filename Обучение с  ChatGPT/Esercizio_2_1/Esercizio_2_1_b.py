#Esercizio 2.1.b
count = 0
while count < 20:
    a = count % 2
    if count == 0:
        print(count, 'non e` divisibile per 2')
    else:
        if a == 0:
            print(count)
    count += 1
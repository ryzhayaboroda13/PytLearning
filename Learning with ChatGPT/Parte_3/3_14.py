#write functione that writes a multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(i * num)
num = int(input("Insert a number to multiplicate : "))
print(multiplication_table(num))
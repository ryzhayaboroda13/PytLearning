#write calculator function
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Can't divide for 0"
        return a / b
    else:
        "You've insered unknown operation"

a = float(input("Insert first number "))
b = float(input("Insert second number "))
operation = input("Insert operation to do + - * / ")
print(calculator(a, b, operation))
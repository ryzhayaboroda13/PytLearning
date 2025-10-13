#write function that controlling password: min 8 characters, alphanumeric
def check_password(password):
    while True:
        if len(password) < 7: 
            print("Length of password isn't enough")
            password = input("Insert new password: ")
        else:    
            if any(char.isdigit() for char in password):
                print("Now password is good")
                break
            else:  
                print("Insert some number")
                password = input("Password must be alphanumeric: ")
password = input("Insert new password: ")
print(check_password(password))
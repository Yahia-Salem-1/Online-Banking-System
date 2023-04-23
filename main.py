from time import sleep
import random
import bank_python

isUsed = True

print("\n\t\tYahia's Online Banking System:\n\n")

def sign_user_choice():
    try:
        print("\n\n1.\tLog In\n")
        print("2.\tSign up\n")
        print("\nType -1 to quit")
        user_choice = int(input("Choose a number from 1-2: "))

        if user_choice == 1:
            log_in()
        elif user_choice == 2:
            sign_up()
        elif user_choice == -1:
            exit_program()
        else:
            print("\nPlease enter a valid number.\n")

    except ValueError:
        print("\nPlease put in only numbers and do not enter empty spaces.")
        return sign_user_choice()

    

def sign_up():
    try:
        f_name = str(input("\nWhat is your first name? "))
        l_name = str(input("\nWhat is your last name? "))

        username = str(input("\nCreate a username: "))

        password = str(input("\nCreate a password: "))
        ver_password = str(input("\nVerify your password: "))
        
        email = str(input("\nEnter an email: ")).lower()

        pin = int(input("\nEnter your pin: "))
    
    except ValueError:
        print("\nPlease enter the value types")
        sign_up()
        
    if password != ver_password:
        print("\nPasswords do not match!\n")
        sign_up()

    elif len(str(pin)) != 4:
        print("\nPin is not the correct length. Must be 4 characters long.")
        sign_up()
    
    elif f_name == "" or l_name == "" or email == "" or password == "" or username == "" or pin == None:
        print("\nOne or more of the input fields are missing. Please try again.")
        sign_up()
    
    elif len(f_name) > 45 or len(l_name) > 45 or len(password) > 45:
        print("\nFirst Name / Last Name / Password must be less than or equal to 45 characters")

    elif len(password) < 4:
        print("\nPassword must be greater than or equal to 4 characters")

    elif len(email) > 100:
        print("\nEmail must be less than or equal to 100 characters")

    elif len(email) < 7:
        print("\nEmail must be greater than or equal to 7 characters")

    else:
        bank_python.sign_user_up(f_name, l_name, username, password, email, pin)
    
def log_in():
    username = str(input("\nEnter username: "))
    password = str(input("\nEnter password: "))
    
    bank_python.log_user_in(username, password)

def bank_account():
    pass 

def withdraw():
    pass

def deposit():
    pass

def exit_program():
    global isUsed
    isUsed = False

while isUsed:
    sign_user_choice()
from time import sleep
import random
import mysql.connector as connector


isUsed = True
connection = connector.connect(host = 'localhost', user = 'root', password = "Seafood@1431", database = "bank")

cursor = connection.cursor()
cursor = connection.cursor(buffered=True)

select_bank_account = ("""SELECT * FROM bank_account""")
select_first_name = ("""SELECT username FROM bank_account""")

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
        sign_user_up(f_name, l_name, username, password, email, pin)
    
def log_in():
    username = str(input("\nEnter username: "))
    password = str(input("\nEnter password: "))
    
    log_user_in(username, password)

def bank_account():
    pass 

def withdraw():
    pass

def deposit():
    pass

def exit_program():
    global isUsed
    isUsed = False
def sign_user_up(first, last, user, passwd, e_mail, pin):
    cursor.execute(select_bank_account)
    insert_required_info = ("""INSERT INTO bank_account(username, password, First_Name, Last_Name, Pin, email) VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}")""".format(user, passwd, first, last, pin, e_mail))
    cursor.execute(insert_required_info)

def log_user_in(user_n, passw):
    cursor.execute(select_bank_account)

    select_username = ("""SELECT username FROM bank_account""")
    select_password = ("""SELECT password FROM bank_account""")
    
    cursor.execute(select_username)

    if cursor == None:
        print("\nThere are no users! Please sign up.")
        sign_up()

    else:
        for item in cursor:
            if item == user_n:
                cursor.execute(select_password)
                for x in cursor:
                    if x == passw:
                        main.bank_account()
                if cursor[-1] != passw:
                    print("\nIncorrect password!")
                    log_in()
        
        
        cursor.execute(select_username) 

        if item in cursor[-1] != user_n:
            print("\nThere are no users with this name!")
            log_in()
    
def test_query():
    cursor.execute(select_first_name)
    for item in cursor:
        print(item)


while isUsed:
    sign_user_choice()


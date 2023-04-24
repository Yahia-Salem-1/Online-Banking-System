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
    select_name = ("""SELECT First_Name, Last_Name FROM bank_account""")
    
    select_name.fetchone()
    item = cursor.execute(select_name)
    user_selection = {
        "1." : "Withdraw Money",
        "2." : "Deposit Money",
        "3." : "Check Balance",
        "4." : "Log out",
        "5." : "Exit program"
    }

    print("\n\nWelcome, {0} {1}".format(item[0], item[1]))

    for key, value in user_selection.items():
        print("{0}\t{1}".format(key, value))

def withdraw():
    pass

def deposit():
    pass

def exit_program():
    global isUsed
    isUsed = False
def sign_user_up(first, last, user, passwd, e_mail, pin):
    cursor.execute(select_bank_account)
    insert_required_info = ("""INSERT INTO bank_account(username, password, First_Name, Last_Name, Pin, email) VALUES(%s, %s, %s, %s, %s, %s)""", (user, passwd, first, last, pin, e_mail))
    

    cursor.execute(insert_required_info)
    connection.commit()

def log_user_in(user_n, passw):
    cursor.execute(select_bank_account)

    select_user_pass = ("""SELECT username, password FROM bank_account""")

    cursor.execute(select_user_pass)

    found_user = False

    if not cursor.fetchone() == None: #shorter than 'if cursor == None:' and makes more sense in code
        print("\nThere are no users! Please sign up.")
        sign_up()
    
    else:
        for i in cursor.fetchall():
            if i[0] == user_n:
                found_user = True
                if i[1] == passw:
                    bank_account()
                else:
                    print("\nIncorrect password!")
                    log_in()
            
        if not found_user:
            print("\nThere are no users with this name!")
            sign_user_choice()
    
def test_query():
    cursor.execute(select_first_name)
    for a in cursor:
        print(a)


while isUsed:
    connection.ping(reconnect=True)
    sign_user_choice()
    


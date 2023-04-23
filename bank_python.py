import mysql.connector as connector
import main

connection = connector.connect(host = 'localhost', user = 'root', password = "Seafood@1431", database = "bank")

cursor = connection.cursor()
cursor = connection.cursor(buffered=True)

select_bank_account = ("""SELECT * FROM bank_account""")
select_first_name = ("""SELECT username FROM bank_account""")

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
        main.sign_up()

    else:
        for item in cursor:
            if item == user_n:
                cursor.execute(select_password)
                for x in cursor:
                    if x == passw:
                        main.bank_account()
                if cursor[-1] != passw:
                    print("\nIncorrect password!")
                    main.log_in()
        
        
        cursor.execute(select_username) 

        if item in cursor[-1] != user_n:
            print("\nThere are no users with this name!")
            main.log_in()
    
def test_query():
    cursor.execute(select_first_name)
    for item in cursor:
        print(item)


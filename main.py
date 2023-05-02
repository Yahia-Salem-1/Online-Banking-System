from time import sleep
import mysql.connector as connector
import random


isUsed = True
def connect():
    global connection, cursor, select_bank_account
    
    connection = connector.connect(user = 'root', password = "root", database = "bank")
    cursor = connection.cursor()
    select_bank_account = ("""SELECT * FROM bank_account""")

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
        sign_user_choice()

    

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
        sign_user_choice()
    
def log_in():
    username = str(input("\nEnter username: "))
    password = str(input("\nEnter password: "))
    
    log_user_in(username, password)
    
def exit_program():
    print("\nThank you for using our app!")
    global isUsed
    isUsed = False
    cursor.close()
    connection.close()

def sign_user_up(first, last, user, passwd, e_mail, pin):
    cursor.execute(select_bank_account)
    insert_required_info = ("""INSERT INTO bank_account(username, password, First_Name, Last_Name, Pin, email) VALUES(%s, %s, %s, %s, %s, %s)""", (user, passwd, first, last, pin, e_mail))
    

    cursor.execute(insert_required_info)
    connection.commit()
    


def log_user_in(user_n, passw):
    cursor = connection.cursor(buffered=True)
    cursor.execute(select_bank_account)
    
    select_user_pass_name = ("""SELECT username, password, First_Name, Last_Name, money FROM bank_account""")

    cursor.execute(select_user_pass_name)
 
    found_user = False

    if not cursor.fetchall(): #shorter than 'if cursor == None:' and makes more sense in code
        print("\nThere are no users! Please sign up.")
        sign_up()
    
    else:
        for i in cursor.fetchone():
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


    def bank_account():
        user_selection = {
            "1." : "Withdraw Money",
            "2." : "Deposit Money",
            "3." : "Check Balance",
            "4." : "ATM Locator",
            "5." : "Log out",
            "6." : "Exit program"
        }

        print("\n\nWelcome, {0} {1}".format(i[2], i[3]))

        for key, value in user_selection.items():
            print("\n{0}\t{1}".format(key, value))
        
        try:
            bank_user_choice = int(input("\nSelect a number (1-5): "))

        except ValueError:
            print("\nPlease enter an integer")
            bank_account()

        if bank_user_choice == 1:
            withdraw()
        
        elif bank_user_choice == 2:
            deposit()
        
        elif bank_user_choice == 3:
            check_balance()

        elif bank_user_choice == 4:
            nearest_ATM()

        elif bank_user_choice == 5:
            sign_user_choice()
        
        elif bank_user_choice == 6:
            exit_program()

        else:
            print("\nPlease enter a number from 1 to 5")
            bank_account()

        def withdraw():
            try:
                qnty = round(float(input("\nHow much do you want to withdraw? ")), 2)
            except ValueError:
                print("\nPlease enter a number!")

            money = float(i[4])

            if money - qnty < 0:
                print("\nYou do not have enough money")
                withdraw()
            elif qnty < 0:
                print("\nYou can deposit instead of withdrawing negative money.")
                deposit()
            else:
                money = float(money - qnty)

                i[4] = money


                

        def deposit():
            try:
                qnty = round(float(input("\nHow much do you want to deposit? ")), 2)
            except ValueError:
                print("\nPlease enter a number!")

            money = float(i[4])

            if qnty < 0:
                print("\nYou can withdraw instead of depositing negative money.")
                withdraw()
            else:
                money = float(money + qnty)

                i[4] = money


        def check_balance():
            print("\n{0} account balance: ${1}".format(i[0], i[4]))
            print("\n'1' to go back to your main dashboard")
            
            try:
                back = int(input(""))
            except ValueError:
                check_balance()

            if back == 1:
                bank_account()
            else: 
                check_balance()

def nearest_ATM():
    number = str(random.randint(100, 99999))
    names = (['advice', 'disease', 'city', 'leader', 'reading', 'refrigerator', 'education', 'equipment', 'apple', 'tradition', 'professor', 'indication', 'nature', 'environment', 'consequence', 'editor', 'ratio', 'software', 'inflation', 'dad', 'village', 'hat', 'uncle', 'assistance', 'hotel', 'shirt', 'variation', 'location', 'winner', 'understanding', 'assistant', 'committee', 'music', 'trainer', 'control', 'news', 'ladder', 'entry', 'recognition', 'difficulty', 'agency', 'efficiency', 'football', 'son', 'cousin', 'engineering', 'pollution', 'health', 'situation', 'chocolate'])
    road_types = ['Fwy', 'Hwy', 'Blvd', 'St', 'Rd', 'Ave', 'Ln', 'Dr', 'Pkwy', 'Trl', 'Cir', 'Ct', 'Pl', 'Ter', 'Expy', 'Way', 'Pk', 'Sq', 'Plz', 'Cove', 'Ally', 'Cres', 'Cswy', 'Pass', 'Bay', 'Gate', 'Grn', 'Hts', 'Knl', 'Mtwy']
    random_names = random.choice(names).capitalize()
    random_types = random.choice(road_types)

    cities_dict = {
        "Pittsburgh": "Pennsylvania",
        "Detroit": "Michigan",
        "Cleveland": "Ohio",
        "Gary": "Indiana",
        "Youngstown": "Ohio",
        "Milwaukee": "Wisconsin",
        "Baltimore": "Maryland",
        "St. Louis": "Missouri",
        "Cincinnati": "Ohio",
        "Chicago": "Illinois",
        "Philadelphia": "Pennsylvania",
        "Buffalo": "New York",
        "Newark": "New Jersey",
        "Kansas City": "Missouri",
        "Louisville": "Kentucky",
        "Birmingham": "Alabama",
        "Memphis": "Tennessee",
        "New Orleans": "Louisiana",
        "Atlanta": "Georgia",
        "Houston": "Texas",
        "Dallas": "Texas",
        "San Antonio": "Texas",
        "Fort Worth": "Texas",
        "Austin": "Texas",
        "El Paso": "Texas",
        "Tulsa": "Oklahoma",
        "Oklahoma City": "Oklahoma",
        "Wichita": "Kansas",
        "Omaha": "Nebraska",
        "Des Moines": "Iowa",
        "Minneapolis": "Minnesota",
        "Duluth": "Minnesota",
        "Grand Rapids": "Michigan",
        "Saginaw": "Michigan",
        "Flint": "Michigan",
        "Buffalo": "West Virginia",
        "Scranton": "Pennsylvania",
        "Hartford": "Connecticut",
        "New Haven": "Connecticut",
        "Providence": "Rhode Island",
        "Worcester": "Massachusetts",
        "Springfield": "Massachusetts",
        "Manchester": "New Hampshire",
        "Portland": "Maine",
        "Concord": "New Hampshire",
        "Burlington": "Vermont",
        "Utica": "New York",
        "Syracuse": "New York",
        "Rochester": "New York",
        "Erie": "Pennsylvania"
    }

    city_prompt = input("\nPlease input your closest major city: ").capitalize()
    state_prompt = ((input("\nPlease input the state it is located in: ")).lower()).capitalize()
    state_list = []
    for key, value in cities_dict.items():
        if value == state_prompt:
            if key == city_prompt:
                correct_city = []
                random_address = f"{number} {random_names} {random_types}, {key}, {value}"
                print("\nNearest ATM: ", random_address)
                correct_city.append(key)
            else:
                state_list.append(key)
    
    
        

    if len(state_list) > 0 and city_prompt != key:
        city = random.choice(state_list)
        print(f"\nThere is an ATM located in {city}.")
    
    elif state_prompt != value and city_prompt != key:
        print("\nWe do not operate in your state of interest.")



if __name__ == '__main__':
    connect()
    while isUsed:
       sign_user_choice()  


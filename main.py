from time import sleep
import random

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
        elif user_choice == 3:
            exit_program()
        else:
            print("\nPlease enter a valid number.\n")

    except ValueError:
        print("\nPlease put in only numbers and do not enter empty spaces.")
        return sign_user_choice()
    


while isUsed:
    sign_user_choice()
from Login import Login
from Register import Register

def MainMenu():
    print("~~~~~~~~~~~~~~~~~ WELCOME TO CROWD FUND APP ~~~~~~~~~~~~~~~~~")
    x = input("please enter 'l' for login or 'r' for register: ")
    if x == 'l':
        Login()
    elif x == 'r':
        Register()
    else:
        print("invalid option")
        MainMenu()

MainMenu()
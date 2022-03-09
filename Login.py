from checkUserData import checkData
from ProjectMenu import projectMenu
def Login():
    print("><><><><><><><>< LOGIN ><><><><><><><><")
    #login using mail and pass
    usrMail = input("please enter your email: ")
    while True:
        if usrMail:
            break
        else:
            usrMail = input("Empty field, please enter your email: ")

    usrPass = input("please enter your password: ")
    while True:
        if usrPass:
            break
        else:
            usrPass = input("Empty field, please enter your password: ")

    if checkData(usrMail,usrPass):
        print("logged in successfully")
        return projectMenu(usrMail)
    print("enter correct data")
    return Login()
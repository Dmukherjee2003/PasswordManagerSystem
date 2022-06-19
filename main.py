from cryptography.fernet import Fernet
import random


print("-------------------------START-------------------------")

'''''

def key():
    keynew = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(keynew)
        '''''


def get_key():
    file = open("key.key", "rb")
    key2 = file.read()
    file.close()
    return key2


a = random.randint(80000, 89999)


def addpwd():
    with open("PassKey_generator.txt", "a") as f:
        f.write(str(a) + "\n")


print("A password file named PassKey_generator.txt has been created please open the file and locate the  new password")
addpwd()
pwd = int(input("Please enter your password: "))

key = get_key()
fer = Fernet(key)


def manage():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user_name, password_f = data.split(":")
            print("Username: " + user_name + " : " + "Password: " + fer.decrypt(password_f.encode()).decode())


def add():
    username = input("Username: ")
    user_password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(username + " : " + fer.encrypt(user_password.encode()).decode() + " \n")


if pwd == a:
    print("Please Choose an Option: ")
    print("\t 1) Add New Password")
    print("\t 2) Manage Old Password")
    print("\t 3) Quit Application")

    repetions = 5

    while repetions != 0:
        print("Enter 3 to quit application")
        user_choice = int(input("Please select an option number: "))
        if user_choice == 1 or 2:
            if user_choice == 1:
                add()
            elif user_choice == 2:
                manage()
            elif user_choice == 3:
                print("Thank you for using the password manager!")
                print("---------------------------END---------------------------")
                quit()
            else:
                print("You have not Entered the correct number please try again")
                repetions = 5
        else:
            repetions = repetions - 1
            print("Please select an appropriate value "
                  "\t you have ", repetions, " tries left")
else:
    print("You did not enter the correct password")
    print("\t System will shut off")
    print("---------------------------END---------------------------")
    quit()

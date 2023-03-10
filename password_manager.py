from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("Key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''
def load_key():
    file = open("Key.key", "rb")
    key  = file.read()
    file.close()
    return key



master_pwd = input("What is the master password? ").lower()

key = load_key()
#key = Fernet.generate_key()
fer = Fernet(key)


def view ():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User Name: " ,user, ",Password: " ,str(fer.decrypt(passw.encode()).decode()))


def add ():
    name = input("Account name: ").lower()
    pwd = input("Password: ").lower()
    with open('password.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")




while True:
    mode = input("would you like to add a new password and view existing ones (view, add) or press q to quite? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Choose a correct mode")
        continue
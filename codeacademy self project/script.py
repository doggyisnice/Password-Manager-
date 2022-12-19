

master_password = "693042"

pwd = input("type in password: ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            account, user, passw = line.split("|")
            print("Account: " + account + " | User: " + user + " | Password: " + passw)                                                          
            

def add():
    platform = input("which account/app/website is this for?: ")
    username = input("account name: ")
    password = input("password: ")
    with open('passwords.txt', 'a') as f:
        f.write(platform + " | " + username + " | " + password + "\n")

while pwd == master_password:
    mode = input("Would you like to add a new password (a) or view existing passwords (v) or quit (q): ")
    if mode == "q":
        break
    if mode == "a":
        add()
    if mode == "v":
        view()
    
else:
    print("passcode incorrect")
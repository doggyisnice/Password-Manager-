from cryptography.fernet import Fernet
import master_pass_encrypted 

#This function loads the key from the current directory named `key.key`
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key  

    

key = load_key() 
fer = Fernet(key)


pwd = input("type in password: ")

#This function generates a key for you
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
# write_key()

#This line decrypts the master password from the master_pass_encrypted.py file and stores it in the variable correct_password
correct_password = master_pass_encrypted.fernet.decrypt(master_pass_encrypted.enc_master_password.encode()).decode()

#   This function encrypts a message
def add():
    platform = input("which account/app/website is this for?: ")
    username = input("account name: ")
    password = input("password: ")
    with open('passwords.txt', 'a') as f: #ab = append binary
        f.write(platform + " | " + username + " | " + fer.encrypt(password.encode()).decode() + "\n")
        print("password added")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            account, user, passw = line.split(" | ")
            print("Account: " + account + " | User: " + user + " | Password: " + fer.decrypt(passw.encode()).decode())                                                          
            
    

while pwd == correct_password:
    mode = input("Would you like to add a new password (a) or view existing passwords (v) or quit (q): ")
    if mode == "q":
        break
    if mode == "a":
        add()
    if mode == "v":
        view()
    
else:
    print("passcode incorrect")
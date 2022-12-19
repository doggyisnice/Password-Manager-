from cryptography.fernet import Fernet
#input your master_password
master_password = ""
key = Fernet.generate_key()
fernet = Fernet(key)
enc_master_password = fernet.encrypt(master_password.encode()).decode()

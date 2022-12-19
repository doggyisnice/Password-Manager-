from cryptography.fernet import Fernet

master_password = "693042"
key = Fernet.generate_key()
fernet = Fernet(key)
enc_master_password = fernet.encrypt(master_password.encode()).decode()

from cryptography.fernet import Fernet


key = Fernet.generate_key()
file = open("encryption_key.txt", 'wb')
file.write(key.decode('utf-8'))
file.close()

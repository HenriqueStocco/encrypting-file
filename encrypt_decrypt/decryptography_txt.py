# Importing module
from cryptography.fernet import Fernet
from cryptography_txt import key

# Using generate key
fernet = Fernet(key)

# Opening original file for encryption
with open('your_file.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

# Decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# saving the decrypted data
with open('your_file.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
# Importing module
from cryptography.fernet import Fernet

# Generating Key
key = Fernet.generate_key()

# Generating a string key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key),filekey.write(key)

# Opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# Using generate key
fernet = Fernet(key)

# Opening original file for encryption
with open('your_file.txt', 'rb') as file:
    original = file.read()

# Encrypting the file
encrypted = fernet.encrypt(original)

# Open the file in write mode and
# save the encrypted data
with open('your_file.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted), encrypted_file.write(encrypted)
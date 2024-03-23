#!/usr/bin/env python3
import base64
from cryptography.fernet import Fernet  # Example of using Fernet encryption

# Encrypt and encode email and password
email = "mohamedx@gmail.com"
password = "mik45A@k"

# Generate a key for encryption (must be kept secret)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt email and password
encrypted_email = cipher.encrypt(email.encode())
encrypted_password = cipher.encrypt(password.encode())

# Base64 encode the encrypted email and password
encoded_email = base64.urlsafe_b64encode(encrypted_email).decode()
encoded_password = base64.urlsafe_b64encode(encrypted_password).decode()

# Construct the URL with encrypted and encoded email and password
url = f"http://127.0.0.1:5005/api/profile/{encoded_email}:{encoded_password}"

print("URL with encrypted and encoded email and password:")
print(url)

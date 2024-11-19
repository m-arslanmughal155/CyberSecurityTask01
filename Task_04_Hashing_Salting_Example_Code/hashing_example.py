import hashlib
import os

def hash_password(password, salt=None):
    if not salt:
        salt = os.urandom(16)
    salted_password = salt + password.encode()
    hashed = hashlib.sha256(salted_password).hexdigest()
    return hashed, salt


password = "password123!@#"  #sample-password

hashed_password, _ = hash_password(password)
print(f"Hashed Password (No Salt): {hashed_password}")

hashed_password_with_salt, salt_used = hash_password(password)
print(f"Hashed Password (With Salt): {hashed_password_with_salt}")

print(f"Salt Used: {salt_used.hex()}")
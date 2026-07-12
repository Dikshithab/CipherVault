import os
import base64
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Fixed salt (for demo project)
SALT = b"CipherVault2026"

def generate_fernet(password):
    password = password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return Fernet(key)


def encrypt_file(filepath, password):

    start_time = time.time()

    fernet = generate_fernet(password)

    with open(filepath, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    filename = os.path.basename(filepath)

    encrypted_path = os.path.join(
        "encrypted",
        filename + ".enc"
    )

    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)

    end_time = time.time()

    stats = {
        "filename": filename,
        "original_size": round(os.path.getsize(filepath)/1024,2),
        "encrypted_size": round(os.path.getsize(encrypted_path)/1024,2),
        "time_taken": round(end_time-start_time,3),
        "algorithm":"Fernet (AES-128)"
    }

    return encrypted_path, stats

def decrypt_file(filepath, password):
    fernet = generate_fernet(password)

    with open(filepath, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    filename = os.path.basename(filepath).replace(".enc", "")
    decrypted_path = os.path.join("decrypted", filename)

    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)

    return decrypted_path
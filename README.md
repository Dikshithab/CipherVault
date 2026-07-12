# 🔐 CipherVault

CipherVault is a secure file encryption and decryption web application built using **Python**, **Flask**, and **Cryptography (Fernet)**. It allows users to encrypt files with a password and decrypt them using the same password, ensuring secure file sharing and storage.

---

## 📸 Preview

> Add screenshots here after running the project.

Example:

![Home Page](screenshots/home.png)

---

# ✨ Features

- 🔐 Password-based file encryption
- 🔓 Secure file decryption
- 🛡️ Fernet (AES-128) encryption
- 🔑 PBKDF2-HMAC-SHA256 password-based key derivation
- 📂 Drag & Drop file upload
- 🌙 Dark Mode
- 📱 Responsive UI
- 📄 Supports multiple file formats
- 🚫 20 MB upload limit
- ⚡ Fast encryption & decryption
- 🎨 Modern Glassmorphism Interface

---

# 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend

- Python
- Flask

### Security

- Cryptography Library
- Fernet Encryption
- PBKDF2-HMAC-SHA256

---

# 📂 Project Structure

```
CipherVault/

│── app.py

│── requirements.txt

│── README.md

│

├── templates/

│ └── index.html

│

├── static/

│ ├── style.css

│ └── script.js

│

├── utils/

│ └── crypto_utils.py

│

├── uploads/

├── encrypted/

└── decrypted/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CipherVault.git
```

Move into the project folder

```bash
cd CipherVault
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🔐 Encryption Workflow

1. User uploads a file.
2. User enters a password.
3. PBKDF2 generates a secure encryption key.
4. Fernet encrypts the file.
5. Encrypted file is downloaded.
6. User uploads the encrypted file.
7. Same password regenerates the key.
8. Original file is restored.

---

# 📖 Supported File Types

- PDF
- TXT
- DOCX
- PNG
- JPG
- JPEG
- CSV
- XLSX
- ENC

---

# 🔒 Security

CipherVault does **not store passwords**.

The password is only used to derive the encryption key during encryption and decryption.

Encryption is performed using **Fernet**, which provides:

- AES-128 Encryption
- Authentication
- Integrity Protection

---

# 🚀 Future Improvements

- User Authentication
- File History
- Multiple Encryption Algorithms
- Cloud Storage Integration
- File Compression
- Password Strength Meter
- Email File Sharing

---

# 👩‍💻 Developer

**Burra Shiva Dikshitha**

Python | Flask | Java | React | Full Stack Development

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://linkedin.com/in/YOUR_PROFILE

---

# ⭐ If you like this project

Give it a ⭐ on GitHub.
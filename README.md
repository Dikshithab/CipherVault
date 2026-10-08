# 🔐 CipherVault – Secure File Encryption & Decryption

> **CipherVault is a cybersecurity-focused web application that securely encrypts and decrypts files using Python Flask and the Fernet symmetric encryption algorithm from the Python Cryptography library.**

The project demonstrates practical implementation of **symmetric encryption, secure key generation, file handling, and web-based security workflows**.

---

# ✨ Features

* 🔑 Secure encryption key generation
* 🔒 File encryption using Fernet
* 🔓 File decryption using the corresponding encryption key
* 📁 Drag & drop file upload
* 📥 Automatic encrypted/decrypted file download
* 🌙 Dark mode
* 📱 Responsive design
* 🔔 Toast notifications
* ⏳ Loading animations
* 🎨 Modern glassmorphism interface

---

# 🔐 Security

CipherVault uses **Fernet symmetric authenticated encryption** provided by the Python Cryptography library.

Fernet provides:

* Confidentiality
* Integrity verification
* Authentication of encrypted data
* Secure key-based encryption and decryption

The same secret key is required to decrypt the encrypted file.

### Encryption Flow

```text
Original File
      │
      ▼
Generate Fernet Key
      │
      ▼
Fernet Encryption
      │
      ▼
Encrypted File
      │
      ▼
Download
```

### Decryption Flow

```text
Encrypted File
      │
      ▼
Provide Correct Key
      │
      ▼
Fernet Decryption
      │
      ▼
Original File
      │
      ▼
Download
```

---

# 🧠 How It Works

### 1. Generate Key

A secure Fernet encryption key is generated.

### 2. Upload File

The user selects or drags a file into the application.

### 3. Encrypt

The application encrypts the file using the generated Fernet key.

### 4. Download

The encrypted file can be downloaded and stored separately.

### 5. Decrypt

The encrypted file and corresponding key are provided to the application.

### 6. Recover Original File

If the correct key is provided, the original file is decrypted and made available for download.

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* Bootstrap Icons

## Backend

* Python
* Flask

## Security

* Python Cryptography Library
* Fernet Symmetric Encryption

---

# 📂 Project Structure

```text
CipherVault/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── uploads/
├── encrypted/
├── decrypted/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── utils/
    ├── key_generator.py
    └── crypto_utils.py
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Dikshithab/CipherVault.git
```

---

## 2. Navigate to Project

```bash
cd CipherVault
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```powershell
venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run Application

```bash
python app.py
```

---

## 7. Open Application

```text
http://127.0.0.1:5000
```

---

# 🧪 Example Workflow

```text
User
 │
 ▼
Generate Encryption Key
 │
 ▼
Select File
 │
 ▼
Encrypt
 │
 ▼
Encrypted File
 │
 ▼
Download
 │
 ▼
Later Upload Encrypted File
 │
 ▼
Provide Encryption Key
 │
 ▼
Decrypt
 │
 ▼
Original File
```

---

# 🔒 Security Considerations

The encryption key is critical to the security of the encrypted file.

If the correct key is lost, the encrypted data cannot be successfully decrypted through the application.

For production use, additional security controls would be required, including:

* Secure key storage
* User authentication
* File size restrictions
* File type validation
* Secure temporary-file handling
* Automatic cleanup of uploaded files
* HTTPS
* Rate limiting
* Access control
* Secure cloud storage

CipherVault is currently designed primarily as an **educational and portfolio cybersecurity project**.

---

# 🚀 Future Enhancements

Potential improvements include:

* User authentication
* Database integration
* Encryption/decryption history
* AES-based encryption support
* Cloud storage integration
* Secure file sharing
* Password-based encryption
* Multi-file encryption
* Automatic temporary-file cleanup
* File integrity verification
* Secure cloud deployment

---

# 🎯 What This Project Demonstrates

CipherVault demonstrates practical understanding of:

```text
Python
  +
Flask
  +
File Handling
  +
Symmetric Encryption
  +
Cryptography Library
  +
Secure Key Generation
  +
Web Application Development
  +
Cybersecurity Concepts
```

---

# 👩‍💻 Developer

**Burra Shiva Dikshitha**

B.Tech — Computer Science Engineering (Cyber Security)

**Skills demonstrated:**

* Python
* Flask
* Cybersecurity
* Cryptography
* Full Stack Development
* Web Development

---

# 📜 License

This project is developed for **educational and portfolio purposes**.

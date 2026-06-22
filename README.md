# 🔐 Advanced Password Security Analyzer

A Python-based cybersecurity tool that analyzes password strength using security best practices and provides detailed feedback to improve password security.

This tool is designed for cybersecurity learning, ethical hacking practice, and password auditing.

---

## 📌 Features

- Password strength scoring system (0–100)
- Checks uppercase, lowercase, digits, special characters
- Detects common weak passwords
- Detects predictable patterns (like 1234, qwerty)
- Provides security improvement suggestions
- Regex-based validation engine
- Lightweight and fast execution
- Generates stronger password suggestions

---

## ⚙️ Installation

```bash
git clone https://github.com/adityainfosec/Password-Strength-Checker.git
cd Password-Strength-Checker
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the tool:

```bash
python3 password_checker.py
```

Enter password:

```text
Enter password: Hello@123
```

Optional username:

```text
Enter username: aditya
```

---

## 📊 Example Output

```text
Password Strength Score: 85/100

✔ Uppercase letters detected  
✔ Lowercase letters detected  
✔ Numbers detected  
✔ Special characters detected  

⚠ Suggestion: Increase password length for better security  

=== AUTO FIXED STRONG PASSWORD ===
CyB@7kQm#92Ld

=== SUGGESTED SECURE PASSWORDS ===
1. Cyber@482A
2. Shield#739X
3. Secure!562A
4. Matrix@901B
5. NetSafe#284D
6. Guard!118P
7. Vault@667Q
8. Cyber#902L
9. Secure@431X
10. Shield!774A
```

---

## 🧠 How It Works

- Takes password input from user  
- Applies regex-based security checks  
- Detects weak patterns and common passwords  
- Calculates strength score (0–100)  
- Generates improved secure password suggestions  
- Helps users understand password security weaknesses  

---

## ⚠️ Disclaimer

This tool is for educational and authorized security testing only.  
Do not use it for malicious or unauthorized activities.

---

## 👨‍💻 Author

Aditya Gupta  
Cybersecurity Enthusiast | Ethical Hacker | Python Security Developer  
GitHub: https://github.com/adityainfosec

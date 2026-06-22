# 🔐 Advanced Password Security Analyzer

A Python-based cybersecurity tool that analyzes password strength using security best practices and provides detailed feedback to improve password security.

This tool is designed for cybersecurity learning, ethical hacking practice, and password auditing.

## 📌 Features

- Password strength scoring system (0–100)  
- Checks uppercase, lowercase, digits, special characters  
- Detects common weak passwords  
- Provides security improvement suggestions  
- Regex-based validation engine  
- Lightweight and fast execution  

## ⚙️ Installation

```bash
git clone https://github.com/adityainfosec/Password-Strength-Checker.git
cd Password-Strength-Checker
pip install -r requirements.txt
```

## 🚀 Usage

Run the tool:

```bash
python3 password_checker.py
```

Enter password:

```text
Enter password: Hello@123
```

## 📊 Example Output

```
Password Strength Score: 85/100

✔ Uppercase letters detected
✔ Lowercase letters detected
✔ Numbers detected
✔ Special characters detected

⚠ Suggestion: Increase password length for better security
```

## 🧠 How It Works

- Takes password input from user  
- Applies regex-based checks  
- Calculates strength score (0–100)  
- Generates security recommendations  

## ⚠️ Disclaimer

This tool is for educational and authorized security testing only.  
Do not use it for malicious or unauthorized activities.

## 👨‍💻 Author

Aditya Gupta  
Cybersecurity Enthusiast | Ethical Hacker | Python Security Developer  
GitHub: https://github.com/adityainfosec

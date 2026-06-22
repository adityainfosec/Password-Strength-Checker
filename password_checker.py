password = input("Enter your password: ")

score = 0
suggestions = []

# Length check
if len(password) >= 8:
    score += 20
else:
    suggestions.append("Increase password length to at least 8 characters")

# Uppercase check
if any(char.isupper() for char in password):
    score += 20
else:
    suggestions.append("Add uppercase letters")

# Lowercase check
if any(char.islower() for char in password):
    score += 20
else:
    suggestions.append("Add lowercase letters")

# Digit check
if any(char.isdigit() for char in password):
    score += 20
else:
    suggestions.append("Add numbers")

# Special character check
if any(not char.isalnum() for char in password):
    score += 20
else:
    suggestions.append("Add special characters")

# Common weak passwords
common_passwords = ["123456", "password", "admin", "qwerty"]
if password.lower() in common_passwords:
    score = 10
    suggestions.append("Avoid common weak passwords")

# Output
print("\nPassword Strength Score:", score, "/100")

if score >= 80:
    print("Strong Password")
elif score >= 50:
    print("Medium Password")
else:
    print("Weak Password")

# Suggestions
if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)

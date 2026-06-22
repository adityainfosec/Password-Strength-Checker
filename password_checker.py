import re
import math
import random
import string

# ---------------- Input ----------------
password = input("Enter password: ")
username = input("Enter username (optional, press enter to skip): ")

print("\n=== ADVANCED SECURITY ANALYSIS REPORT ===\n")

score = 0
suggestions = []

# ---------------- Character Sets ----------------
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

pool_size = 0

# ---------------- Checks ----------------
def check_and_score(condition, add, msg):
    global score
    if condition:
        score += add
    else:
        suggestions.append(msg)

# Length
check_and_score(len(password) >= 14, 25, "Use at least 14 characters for strong security")

# Upper
check_and_score(any(c.isupper() for c in password), 10, "Add uppercase letters")

# Lower
check_and_score(any(c.islower() for c in password), 10, "Add lowercase letters")

# Digits
check_and_score(any(c.isdigit() for c in password), 10, "Add numbers")

# Symbols
check_and_score(any(not c.isalnum() for c in password), 15, "Add special characters")

# Pool size for entropy
if any(c.islower() for c in password): pool_size += 26
if any(c.isupper() for c in password): pool_size += 26
if any(c.isdigit() for c in password): pool_size += 10
if any(not c.isalnum() for c in password): pool_size += 30

# ---------------- Weak patterns ----------------
if re.search(r"(.)\1{2,}", password):
    score -= 10
    suggestions.append("Avoid repeated characters (aaa, 111)")

if re.search(r"1234|abcd|qwerty|asdf", password.lower()):
    score -= 15
    suggestions.append("Avoid predictable keyboard or numeric sequences")

# username similarity
if username and username.lower() in password.lower():
    score -= 20
    suggestions.append("Password should not contain your username")

# common passwords
common = {"123456","password","admin","qwerty","123456789","welcome","letmein"}
if password.lower() in common:
    score = 5
    suggestions.append("Extremely common password detected")

# ---------------- ENTROPY CALCULATION ----------------
def calc_entropy(length, pool):
    if pool == 0:
        return 0
    return round(length * math.log2(pool), 2)

entropy = calc_entropy(len(password), pool_size)

# ---------------- Crack time estimation ----------------
def crack_time(entropy_bits):
    guesses_per_sec = 1e9  # rough GPU assumption
    total = 2 ** entropy_bits
    seconds = total / guesses_per_sec

    if seconds < 60:
        return "Instantly crackable"
    elif seconds < 3600:
        return "Few minutes"
    elif seconds < 86400:
        return "Few hours"
    elif seconds < 31536000:
        return "Few years"
    else:
        return "Centuries or more"

crack = crack_time(entropy)

# ---------------- Score limit ----------------
score = max(0, min(score, 100))

# ---------------- Output ----------------
print("Password Strength Score:", score, "/100")

if score >= 80:
    print("Status: STRONG")
elif score >= 50:
    print("Status: MEDIUM")
else:
    print("Status: WEAK")

print("\nEntropy:", entropy, "bits")
print("Estimated Crack Time:", crack)

# ---------------- Suggestions ----------------
if suggestions:
    print("\nSecurity Issues:")
    for s in suggestions:
        print("-", s)

# ---------------- Password Generator (SMART) ----------------
print("\n=== SMART PASSWORD SUGGESTIONS ===")

def smart_password():
    base = random.choice(["Secure", "Cyber", "Shield", "Matrix", "NetSafe", "Guard"])
    return base + random.choice(symbols) + str(random.randint(10, 99)) + random.choice(upper)

for i in range(10):
    print(f"{i+1}. {smart_password()}")

# ---------------- Summary ----------------
print("\n=== SUMMARY ===")
print("Entropy based security analysis completed")
print("Always use long + random + unique passwords")

import re

def analyze_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Check some common passwords
    common_passwords = [
        "password", "123456", "qwerty",
        "password123", "admin", "letmein"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid commonly used passwords.")

    # Determine strength
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, score, suggestions


print("=== Password Strength Analyzer ===")

password = input("Enter a password to analyze: ")

strength, score, suggestions = analyze_password(password)

print("\nPassword Strength:", strength)
print("Score:", score, "/ 6")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nExcellent! Your password meets all strength requirements.")

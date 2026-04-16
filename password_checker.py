# Password Strength Checker

# Function to evaluate password strength
def check_password_strength(password):
    strength = "Weak"

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        has_number = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_special = any(not char.isalnum() for char in password)

        # Strong password conditions
        if has_number and has_upper and has_special:
            strength = "Strong"
        # Medium password conditions
        elif has_number or has_upper:
            strength = "Medium"

    return strength


# Example password
password = "Medha@123"

# Check strength
result = check_password_strength(password)

# Output result
print(f"Password Strength: {result}")

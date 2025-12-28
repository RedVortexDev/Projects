password = input("Enter your password: ")

strength = 0

# Length
if 8 <= len(password) <= 11:
    strength += 1
elif len(password) >= 12:
    strength += 2
    
# Common words
if password.lower() in ['admin', '1234']:
    strength -= 2
    
    
# Complexity
symbols = "!@#$%^&*()_+"
strength += any(char.islower() for char in password)
strength += any(char.isupper() for char in password)
strength += any(char.isdigit() for char in password)
strength += any(char in symbols for char in password)
    
if strength <= 0:
    print("Password is weak")
elif strength <= 3:
    print("Password is moderate")
else:
    print("Password is strong")
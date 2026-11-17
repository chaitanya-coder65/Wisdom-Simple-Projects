
import random
import string


def generate_password(length, upper, lower, digits, symbols):

    characters = ""

    if upper:
        characters += string.ascii_uppercase

    if lower:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    if length < 4:
        return None

    password = []

    
    if upper:
        password.append(random.choice(string.ascii_uppercase))

    if lower:
        password.append(random.choice(string.ascii_lowercase))

    if digits:
        password.append(random.choice(string.digits))

    if symbols:
        password.append(random.choice(string.punctuation))

    # Fill remaining positions
    for i in range(length - len(password)):
        password.append(random.choice(characters))

    # Shuffle password characters
    random.shuffle(password)

    return ''.join(password)


# Function to check password strength
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


# Main program
def main():

    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length < 4 or length > 128:
            print("Password length must be between 4 and 128.")
            return

        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'

        lower = input("Include lowercase letters? (y/n): ").lower() == 'y'

        digits = input("Include numbers? (y/n): ").lower() == 'y'

        symbols = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(
            length, upper, lower, digits, symbols
        )

        if password is None:
            print("Please select at least one character type.")
            return

        print("\nGenerated Password:", password)

        strength = check_strength(password)

        print("Password Strength:", strength)

    except ValueError:
        print("Please enter a valid number.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

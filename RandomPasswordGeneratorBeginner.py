import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected for password generation.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    # Get user input for password length and character types
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive number.")
        
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate and display password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

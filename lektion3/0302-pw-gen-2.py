import random
import string

def generate_password(length, include_upper, include_lower, include_digits, include_special):
    # Skapa en lista med tecken baserat på användarens val
    all_characters = ''
    if include_upper:
        all_characters += string.ascii_uppercase
    if include_lower:
        all_characters += string.ascii_lowercase
    if include_digits:
        all_characters += string.digits
    if include_special:
        all_characters += string.punctuation
    
    # Om inga tecken valts, ge ett meddelande och avsluta
    if not all_characters:
        print("Du måste välja minst en typ av tecken.")
        return None
    
    # Generera lösenordet genom att slumpmässigt välja tecken
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def save_password_to_file(password, filename="password.txt"):
    with open(filename, "w") as file:
        file.write(password)
    print(f"Lösenordet har sparats till {filename}.")

def main():
    # Fråga användaren om längd på lösenordet
    length = int(input("Ange längden på lösenordet: "))
    
    # Fråga användaren om vilka typer av tecken som ska ingå
    include_upper = input("Vill du inkludera stora bokstäver (A-Z)? (ja/nej): ").strip().lower() == 'ja'
    include_lower = input("Vill du inkludera små bokstäver (a-z)? (ja/nej): ").strip().lower() == 'ja'
    include_digits = input("Vill du inkludera siffror (0-9)? (ja/nej): ").strip().lower() == 'ja'
    include_special = input("Vill du inkludera specialtecken (t.ex. !, @, #)? (ja/nej): ").strip().lower() == 'ja'
    
    # Generera lösenordet
    password = generate_password(length, include_upper, include_lower, include_digits, include_special)
    
    if password:
        print(f"Det genererade lösenordet är: {password}")
        
        # Fråga om användaren vill spara lösenordet
        save_choice = input("Vill du spara lösenordet till en fil? (ja/nej): ").strip().lower()
        if save_choice == 'ja':
            filename = input("Ange filnamn (t.ex. password.txt): ").strip()
            if not filename:
                filename = "passwords.txt"
            save_password_to_file(password, filename)
        else:
            print("Lösenordet sparades inte.")
    
if __name__ == "__main__":
    main()


import secrets
import string

def generate_secure_password(length):
    # Lista med möjliga tecken (stora och små bokstäver, siffror, specialtecken)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generera ett slumpmässigt lösenord
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# Be användaren om längd på lösenordet
while True:
    try:
        length = int(input("Ange längden på lösenordet (t.ex. 12): "))
        if length < 1:
            print("Längden måste vara ett positivt tal.")
        else:
            break
    except ValueError:
        print("Var vänlig ange ett giltigt heltal.")

# Skapa och visa lösenordet
password = generate_secure_password(length)
print("Ditt lösenord är:", password)

import random  # Importerar random-modulen som används för att generera slumpmässiga tal.

random_number = random.randint(1, 100)  # Genererar ett slumpmässigt tal mellan 1 och 100 och sparar det i variabeln random_number.

guess = int(input("Gissa: "))  # Ber användaren att gissa ett tal och konverterar användarens inmatning till ett heltal.

while guess != random_number:  # Startar en loop som fortsätter tills användarens gissning är lika med det slumpmässiga talet.
    if guess > random_number:  # Om användarens gissning är större än det slumpmässiga talet:
        print("För högt")  # Skriv ut "För högt" för att indikera att gissningen var för hög.
    elif guess < random_number:  # Om användarens gissning är mindre än det slumpmässiga talet:
        print("För lågt")  # Skriv ut "För lågt" för att indikera att gissningen var för låg.
    
    guess = int(input("Gissa: "))  # Ber användaren att gissa ett nytt tal och konverterar inmatningen till ett heltal.

print("Klart!")  # När användaren gissar rätt, skriv ut "Klart!" för att indikera att spelet är slut.

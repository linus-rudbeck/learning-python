name = input("Skriv in namn: ")
age = int(input("Skriv in ålder: "))

print(f"Hej {name}! Din ålder är {age}")


if age < 15:
    print("Du får inte ta körkort eller övningsköra")
elif age < 18:
    print("Du får inte ta körkort men du får övningsköra")
else:
    print("Du får ta körkort")
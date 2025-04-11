name = input("Skriv in ett namn: ")
count_to = int(input("Mata in ett tal att räkna till: "))

print(f"Hej {name}!")
print(f"Räknar till {count_to}...")


for count in range(count_to):
    print(count + 1)




while name != "Linus":
    name = input("Namn: ")

print("Klar!")
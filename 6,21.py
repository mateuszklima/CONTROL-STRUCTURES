amount = int(input("Podaj kwotę w PLN: "))

print(f"Kwota {amount} zł w monetach.")

coins_5 = amount // 5
amount = amount % 5

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount

print("5 zł monety:", coins_5)
print("2 PLN monety:", coins_2)
print("1 zł monety:", coins_1)

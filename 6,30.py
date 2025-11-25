# Tworzymy kupon loteryjny 7x7
rows = 7
cols = 7

for i in range(1, rows + 1):  # wiersze
    for j in range(cols):     # kolumny
        number = i + 7 * j
        print(f"{number:2}", end=" ")  # :2 ustawia szerokość na 2 znaki
    print()  # nowy wiersz

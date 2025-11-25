# Pobranie liczby pierwszych liczb do wydrukowania
N = int(input("Podaj liczbę N: "))

count = 0       # licznik znalezionych liczb pierwszych
num = 2         # liczba do sprawdzenia, zaczynamy od 2

while count < N:
    is_prime = True  # zakładamy, że liczba jest pierwsza
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        count += 1
    num += 1

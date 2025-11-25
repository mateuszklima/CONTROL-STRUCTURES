import random

# Losujemy 20 liczb całkowitych od 5 do 10
for _ in range(20):
    number = random.randint(5, 10)  # randint(a, b) zwraca liczbę z przedziału [a, b]
    print(number, end=' ')

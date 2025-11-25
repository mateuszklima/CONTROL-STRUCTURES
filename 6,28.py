# Liczba wyrazów do wydrukowania
n = 20

# Pierwsze dwa wyrazy ciągu
a, b = 0, 1

# Wydruk pierwszego wyrazu
print(a, end=' ')

# Pętla drukująca kolejne wyrazy
for _ in range(1, n):
    print(b, end=' ')
    a, b = b, a + b  # aktualizacja wartości a i b

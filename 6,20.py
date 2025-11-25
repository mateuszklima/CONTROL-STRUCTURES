# Decimal to binary converter

number = int(input("Wpisz liczbę dziesiętną: "))

original = number          # zapamiętujemy liczbę do wyświetlenia
binary_digits = []         # lista na reszty z dzielenia

# Konwersja
while number > 0:
    remainder = number % 2
    binary_digits.append(str(remainder))   # dodajemy resztę
    number //= 2                           # dzielenie całkowite przez 2

# Odwracamy kolejność reszt
binary_digits.reverse()

# Łączymy cyfry w jeden napis
binary_number = "".join(binary_digits)

print(f"{original}(10) = {binary_number}(2)")

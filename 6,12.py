###
# Online store discount calculator
#

# Wczytanie danych
num_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter product price: "))

# Obliczenie kwoty do zapłaty
if num_products <= 2:
    total_amount = num_products * product_price
else:
    # Pierwsze 2 produkty pełna cena
    full_price = 2 * product_price
    # Pozostałe produkty z 25% rabatem
    discounted_price = (num_products - 2) * product_price * 0.75
    total_amount = full_price + discounted_price

print(f"Amount to pay: {total_amount:.2f}")

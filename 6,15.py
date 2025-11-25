###
# EAN-13 checker
#

ean = input("Wpisz numer artykułu EAN-13: ")

# Sprawdzenie, czy numer ma dokładnie 13 cyfr
if len(ean) == 13 and ean.isdigit():
    print("Numer artykułu jest poprawny")
    
    # Sprawdzenie, czy produkt pochodzi z Polski
    if ean[:3] == "590":
        print("Artykuł wyprodukowany w Polsce")
else:
    print("Numer artykułu jest niepoprawny")

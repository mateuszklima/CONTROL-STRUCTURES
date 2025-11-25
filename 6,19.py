ankieta1 = input("Interesujesz się informatyką? (t/n):")
ankieta2 = input("Lubisz grać w gry komputerowe? (t/n):")
ankieta3 = input("Masz konto na Instagramie? (t/n):")

zainteresowany = (ankieta1 == 't')
lubi_grac = (ankieta2 == 't')
ma_insta = (ankieta3 == 't')

print("WYNIKI ANKIETY")


print("Zainteresowany informatyką:", "Tak" if zainteresowany else "Nie")
print("Granie w gry komputerowe:", "Tak" if lubi_grac else "Nie")
print("Posiada konto na Instagramie:", "Tak" if ma_insta else "Nie")

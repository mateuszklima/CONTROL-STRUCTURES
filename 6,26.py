correct_pin = "0805"  # poprawny PIN
attempts = 0           # liczba prób
max_attempts = 3       # maksymalna liczba prób

while attempts < max_attempts:
    entered_pin = input("Wpisz kod PIN: ")
    if entered_pin == correct_pin:
        print("PIN poprawny. Dostęp przyznany.")
        break  # kończymy pętlę, jeśli PIN jest poprawny
    else:
        print("Niepoprawne...")
        attempts += 1

# Sprawdzenie czy użytkownik wyczerpał próby
if attempts == max_attempts:
    print("Przepraszamy, Twoja karta płatnicza została zablokowana.")

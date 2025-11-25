time_24 = input("Wprowadź czas (format 24-godzinny, hh:mm): ")

# Rozdzielamy godzinę i minuty
hour, minute = time_24.split(':')
hour = int(hour)

# Określamy AM/PM i przeliczamy godzinę
if hour == 0:
    hour_12 = 12
    period = "AM"
elif 1 <= hour <= 11:
    hour_12 = hour
    period = "AM"
elif hour == 12:
    hour_12 = 12
    period = "PM"
else:
    hour_12 = hour - 12
    period = "PM"

print(f"Czas w formacie 12-godzinnym: {hour_12}:{minute} {period}")

# Sums numbers entered by user and calculates the average
#
total_sum = 0
count = 0  # Liczba wprowadzonych liczb (bez zera)

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    
    total_sum += number
    count += 1  # Zwiększamy licznik wprowadzonych liczb

# Obliczamy średnią, tylko jeśli wprowadzono jakieś liczby
if count > 0:
    average = total_sum / count
else:
    average = 0

print(f"The total sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")

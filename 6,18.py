x = float(input("Podaj współrzędną x: "))
y = float(input("Podaj współrzędną y: "))

if x == 0 and y == 0:
    print("Punkt P (0,0) znajduje się w początku układu współrzędnych.")
elif x == 0:
    print(f"Punkt P ({x},{y}) znajduje się na osi Y.")
elif y == 0:
    print(f"Punkt P ({x},{y}) znajduje się na osi X.")
elif x > 0 and y > 0:
    print(f"Punkt P ({x},{y}) znajduje się w pierwszej ćwiartce układu współrzędnych.")
elif x < 0 and y > 0:
    print(f"Punkt P ({x},{y}) znajduje się w drugiej ćwiartce układu współrzędnych.")
elif x < 0 and y < 0:
    print(f"Punkt P ({x},{y}) znajduje się w trzeciej ćwiartce układu współrzędnych.")
else:
    print(f"Punkt P ({x},{y}) znajduje się w czwartej ćwiartce układu współrzędnych.")

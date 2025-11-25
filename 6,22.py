for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("BINGO", end=" ")
    elif i % 3 == 0:
        print("TRZY", end=" ")
    elif i % 5 == 0:
        print("PIĘĆ", end=" ")
    else:
        print(i, end=" ")

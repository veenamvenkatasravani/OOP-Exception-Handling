try:
    num = int(input("Entera num: "))
except ValueError:
    print("Invalid input")
else:
    print("Square:", num ** 2)
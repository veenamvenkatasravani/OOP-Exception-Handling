try:
    print("Outer try started")

    try:
        number = int(input("Enter a number: "))
        print(100 / number)

    except ZeroDivisionError:
        print("Inner: Cannot divide by zero")

except ValueError:
    print("Outer: Invalid number")

print("Program completed")
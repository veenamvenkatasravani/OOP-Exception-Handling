def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = divide_numbers(a, b)

except ValueError as error:
    print("Error:", error)

else:
    print("Division result:", result)

finally:
    print("Division operation completed")
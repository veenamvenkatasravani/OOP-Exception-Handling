#The raise statement allows you to raise an exception explicitly when a condition is invalid.

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative")

print("Age:", age)
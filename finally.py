try:
    num =10*2
    print("Result:", num)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program Completed")
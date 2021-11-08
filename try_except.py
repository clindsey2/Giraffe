
try:
    # answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as divide_err:
    print(divide_err)
except ValueError as input_value_err:
    print(input_value_err)

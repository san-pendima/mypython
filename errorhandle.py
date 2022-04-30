try:
    raise ArithmeticError("Just for fun...")
except ZeroDivisionError as zde:
    print(zde)
else:
    print("Iam always associated with try block...")
finally:
    print("Finally block executes at any cost....")
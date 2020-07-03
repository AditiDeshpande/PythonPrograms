import sys

try:
    x = int(input("X : "))
    y = int(input("Y : "))
except ValueError:
    print("Invalid input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can not divide by zero.")
    sys.exit(1)

print(f" {x} / {y} = {result}")

# X = 10 Y = 0 Divide by zero error
# How to handle exceptions
#Following is the exception thrown
# Traceback (most recent call last):
#   File "exceptions.py", line 7, in <module>
#     result = x / y
# ZeroDivisionError: division by zero
#Output for non exceptional values
# X : 4
# Y : 5
#  4 / 5 = 0.8
#Output another exception
# X : ad
# Traceback (most recent call last):
#   File "exceptions.py", line 3, in <module>
#     x = int(input("X : "))
# ValueError: invalid literal for int() with base 10: 'ad'
#For this added try catch while accepting input from user
#Output
# X : da
# Invalid input.

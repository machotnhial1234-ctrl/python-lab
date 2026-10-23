
def square(n):
    """Return the square of a number."""
    return n ** 2


def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32
notepad src\main.py
from utils import square, is_even, celsius_to_fahrenheit

number = int(input("Enter a number: "))

print("Square:", square(number))

if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")

fahrenheit = celsius_to_fahrenheit(number)
print(f"Fahrenheit equivalent: {fahrenheit:.2f} F")

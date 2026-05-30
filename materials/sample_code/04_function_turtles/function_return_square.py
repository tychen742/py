# Fruitful functions generate a value as a result of the function execution.
import turtle


def do_square (number):
    number_square = number * number
    # print("The square of", number, "is", result)
    return number_square

toSquare = int (input("Please enter a number."))

result = do_square(toSquare)

print(result)
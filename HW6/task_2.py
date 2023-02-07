import math


def square_function(side):
    """
    Find the perimeter of the square, the area of the square, and the diagonal of the square
    """
    perimeter = 4 * side
    area = side * 2
    diagonal = side * math.sqrt(2)
    return (perimeter, area, diagonal)


print(square_function(3))

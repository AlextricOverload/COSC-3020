# Solution.py
# COSC-3020-01
# Lab Practice 2
# Alexander Warren
# 4 February 2026

def main():
    # Take in user input
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    # Find which integer is the smallest and which is the largest
    if width < height:  # The width is smaller than the height
        smallest = width
        largest = height
    else:  # The height is smaller than the width, or they're the same
        smallest = height
        largest = width

    # Find the side length and the number of squares
    squares = find_squares(smallest, largest)

    print(squares)


# Finds the side length and number of squares to cover the rectangle
# Returns [side length, number of squares]
def find_squares(smallest: int, largest: int) -> list[int]:
    # First check if width = height
    if smallest == largest:  # The rectangle is already a square
        return [smallest, 1]

    # Otherwise, we need to calculate the answer
    area = int(largest * smallest)  # Area of the rectangle
    remainder = largest % smallest  # Find the first remainder

    # Use the Euclidian Algorithm to find the Greatest Common Denominator (GCD)
    while remainder != 0:
        # Euclidian algorithm replacement
        largest = smallest
        smallest = remainder  # Will ultimately reach the value of the GCD

        remainder = largest % smallest  # Find the next remainder

    # The GCD stored in 'smallest' is our side length
    # Find how many squares are needed
    num_squares = int(area / (pow(smallest, 2)))  # Div. the area of the rectangle by the area of each square
    return [smallest, num_squares]

if __name__ == "__main__":
    main()
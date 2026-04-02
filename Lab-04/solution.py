# solution.py
# Alex Warren
# COSC 3020 Lab Practice 4
# Last Modified 2026-03-01

def main():
    # Establish test values
    # Test 1 & 2: Example values
    matrix1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],
              [18,21,23,26,30]]  # Example matrix
    target1 = 5  # Example 1: Match, should return True
    target2 = 20  # Example 2: No match, should return False

    # Test 3 & 4: Largest/smallest value
    target3 = 30  # Target is the largest value of matrix1
    target4 = 1  # Target is the smallest value of matrix1

    # Tests 5 & 6: Single element
    matrix2 = [[5]]
    target5 = 5  # Match
    target6 = 10  # No match

    # Perform tests and print results
    print(search_matrix(matrix1, target1))  # Expected: True
    print(search_matrix(matrix1, target2))  # Expected: False
    print(search_matrix(matrix1, target3))  # Expected: True
    print(search_matrix(matrix1, target4))  # Expected: True
    print(search_matrix(matrix2, target5))  # Expected: True
    print(search_matrix(matrix2, target6))  # Expected: False


def search_matrix(matrix,target) -> bool:
    """
    Searches for a target value in a given matrix
    :param matrix: The matrix to be searched
    :param target: The target value
    :return: True or False
    """
    # Make sure the matrix actually contains data
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)  # Number of rows in the matrix
    cols = len(matrix[0])  # Number of columns in the matrix

    # Start in the top-right corner
    r = 0
    c = cols - 1

    # Search through the matrix
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:  # Target must be to the left
            c -= 1  # Move column pointer accordingly
        else:  # Target is below
            r += 1  # Move row pointer accordingly

    # If the loop is exited without returning true, target is not in matrix
    return False

# Call main
if __name__ == '__main__':
    main()
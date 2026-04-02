# solution.py
# Alex Warren
# COSC 3020 Lab Practice 5
# Last Modified 2026-03-02

def main():
    # Test: Example inputs
    citations = [3,0,6,1,5]  # Input list
    print(h_index(citations))  # Expected output: 3
    citations = [1,3,1]
    print(h_index(citations))  # Expected output: 1

    # Test Case: All Zero Citations
    citations = [0,0,0]
    print(h_index(citations))  # Expected output: 0


def h_index(citations: list[int]) -> int:
    """
    Takes in a list of citations and returns the h-index of the citations
    :param citations: The list of citations per paper
    :type citations: list[int]
    :return: The h-index of the citations
    :rtype: int
    """
    n = len(citations)  # The number of papers
    counts = [0] * (n+1)  # For every i < n, counts[i] = the number of papers with exactly i citations

    # Count the frequency of citations
    for c in citations:  # c = the number of citations for the specific paper
        if c >= n:  # The current paper's citation count exceeds the number of papers
            counts[n] += 1  # counts[n] = the number of papers with n or more citations
        else:
            counts[c] += 1

    # Iterate backwards to find the h-index
    total_papers = 0
    for i in range(n, -1, -1):
        total_papers += counts[i]
        if total_papers >= i:  # There are at least i papers with at least i citations
            return i

    return 0


if __name__ == '__main__':
    main()

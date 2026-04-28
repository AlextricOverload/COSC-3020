# solution.py
# COSC 3020
# Lab Practice 11
# Author: Alexander Warren
# Last Modified (YYYY-MM-DD): 2026-04-28

from typing import List

def main():
    print(f" It takes {move([1, 0, 5])} move(s). Expect 3")  # Expect 3
    print(f"It takes {move([0, 3, 0])} move(s). Expect 2")  # Expect 2
    print(f"It takes {move([0, 2, 0])} move(s). Expect -1")  # Expect -1


def move(machines: List[int]) -> int:
    """
    Calculates the minimum number of moves to equalize the number of dresses in washing machines

    Each move consists of choosing any number of machines and passing one dress from each chosen machine
    to an adjacent machine. The goal is for every machine to end up with an equal number of dresses
    (total dresses / n).
    :param machines: A list representing the current number of dresses in each machine
    :return: The minimum moves required or -1 if equalization is impossible
    :Note: The complexity is O(n) as it requires a single pass. The logic uses a 'balance' accumulator
    to track the net flow of dresses required across each point in the array.
    """

    n = len(machines)  # The number of washing machines

    # The total number of items must be divisible by the number of machines
    if sum(machines) % n != 0:
        return -1  # It's impossible to have all machines be equal

    target = sum(machines) // n  # The target value for all machines to reach
    balance = 0  # The net flow of dresses that must pass through machine i and i+1 to reach equilibrium
    max_moves = 0  # Return value: how many moves it takes to balance the machines

    for i in range(n):
        diff = machines[i] - target  # How many dresses this specific machine is above or below the target
        balance += diff
        max_moves = max(max_moves, abs(balance), diff)  # The maximum of potential bottlenecks

    return max_moves

if __name__ == "__main__":
    main()
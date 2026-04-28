# solution.py
# COSC 3020
# Lab Practice 11
# Author: Alexander Warren
# Last Modified (YYYY-MM-DD): 2026-04-28

from typing import List

def move(machines: List[int]) -> int:
    n = len(machines)  # The number of washing machines

    # The total number of items must be divisible by the number of machines
    if sum(machines) % n != 0:
        return -1  # It's impossible to have all machines be equal

    target = sum(machines) // n  # The target value for all machines to reach
    balance = 0  
    max_moves = 0  # Return value: how many moves it takes to balance the machines

    for i in range(n):
        diff = machines[i] - target
        balance += diff
        max_moves = max(max_moves, abs(balance), diff)

    return max_moves
# solution.py
# COSC 3020
# Lab Practice 12
# Author: Alexander Warren
# Last Modified(YYYY-MM-DD): 2026-05-6

"""
P(a,b,n) = probability that Player A wins from state (a,b)
= 1.0 if a == n (A already won)
= 0.0 if b == n (B already won)
= 0.5 * P(a+1,b,n) + 0.5 * P(a,b+1,n) otherwise
"""

from typing import Tuple

def prob_rec(a: int, b: int, n: int) -> float:
    if a == n:
        return 1.0
    elif b == n:
        return 0.0
    else:
        return 0.5 * (prob_rec(a+1, b, n) + prob_rec(a, b+1, n))

def prob_dp(a: int, b: int, n: int) -> float:
    # Allocate table of size (n+1)*(n+1)
    dp = [[0.0] * (n+1) for _ in range(n+1)]

    # Our base cases
    for i in range(n):
        dp[n][i] = 1.0
    for j in range(n):
        dp[j][n] = 0.0
    dp[n][n] = 1.0

    # Fill up the table
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            dp[i][j] = 0.5 * dp[i+1][j] + 0.5 * dp[i][j+1]

    # return
    return dp[a][b]

def payout(a: int, b: int, n: int, pot: int) -> Tuple[float, float]:
    p_a: float = prob_dp(a, b, n)
    share_a: float = round(pot * p_a, 2)
    share_b: float = round(pot - share_a, 2)

    return share_a, share_b

def main():
    print(
        f"Example 1: prob_rec(8, 6, 10) = {prob_rec(8, 6, 10)} (Player A wins 81.25% of the time)"
    )
    print(f"Example 2: prob_rec(9, 8, 10) = {prob_rec(9, 8, 10)}")
    print(f"Example 3: prob_rec(0, 0, 3) = {prob_rec(0, 0, 3)}")

    print("-" * 70)

    print(f"prob_dp(8, 6, 10) = {prob_dp(8, 6, 10)}")
    print(f"prob_dp(9, 8, 10) = {prob_dp(9, 8, 10)}")
    print(f"prob_dp(0, 0, 1) = {prob_dp(0, 0, 1)}")
    print(f"prob_dp(0, 0, 3) = {prob_dp(0, 0, 3)}")

    print("-" * 70)

    print(f"payout(8, 6, 10, 100) = {payout(8, 6, 10, 100)}")
    print(f"payout(9, 8, 10, 200) = {payout(9, 8, 10, 200)}")


if __name__ == "__main__":
    main()

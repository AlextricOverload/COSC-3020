# solution.py
# COSC 3020
# Lab Practice 12
# Author: Alexander Warren
# Last Modified(YYYY-MM-DD): 2026-04-28

"""
P(a,b,n) = probability that Player A wins from state (a,b)
= 1.0 if a == n (A already won)
= 0.0 if b == n (B already won)
= 0.5 * P(a+1,b,n) + 0.5 * P(a,b+1,n) otherwise
"""
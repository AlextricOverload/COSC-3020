# solution.py
# COSC 3020
# Lab Practice 8
# Author: Alexander Warren
# Last Modified (YYYY-MM-DD): 2026-04-02

# Imports
import heapq
from typing import Dict, List, Tuple

def signal_times(times: List[List[int]], n: int, k: int) -> int:
    graph = adjacency(times)
    return 0


def adjacency(times: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
    adj = {}

    for edge in times:
        src, dest, time = edge
        if src not in adj:
            adj[src] = []

        adj[src].append((dest, time))

    return adj
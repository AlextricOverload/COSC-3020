# solution.py
# COSC 3020
# Lab Practice 8
# Author: Alexander Warren
# Last Modified (YYYY-MM-DD): 2026-04-02

# Imports
import heapq
from typing import Dict, List, Tuple

def signal_times(times: List[List[int]], n: int, k: int) -> int:
    """
    Calculates the minimum times for all nodes to receive a signal using Dijkstra's algorithm.

    Implements a greedy approach to find the shortest path from a
    starting node `k` to all other `n` nodes in a directed graph.

    :param times: A list of directed edges, each edge listed as [source, target, cost]
    :param n: The total number of nodes in the graph (1 to n).
    :param k: The starting node where every signal is sent from
    :return: The time it takes for all nodes to receive a signal, or -1 if unreachable.
    """
    graph = adjacency(times)
    pq = []

    # Initialize distances with infinity per Dijkstra's algorithm
    dist = [float('inf')] * (n + 1)
    dist[k] = 0  # Distance to the starting node is 0

    # Heap sorting
    heapq.heappush(pq, (dist[k], k))

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if we've already found a shorter path to u
        if d > dist[u]:
            continue

        # Relax edges: check if passing through 'u' is a shortcut to 'v'
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    res = max(dist[1:])
    if res < float('inf'):  # All nodes have been visited
        return int(res)
    else:  # One or more nodes were unreachable
        return -1


def adjacency(times: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
    """
    Converts a flat list of edges into an Adjacency List (Dictionary).
    :param times: A list of directed edges, each edge listed as [source, target, cost]
    :return: A dictionary where keys are source nodes and values are lists of
            (target, cost) tuples. This allows O(1) access to a neighbor.
    """
    adj = {}  # Our adjacency list

    # Convert the edge list into a dictionary
    for edge in times:
        src, dest, time = edge
        if src not in adj:
            adj[src] = []

        adj[src].append((dest, time))

    return adj

# Solution testing function
def tests() :
    # Test 1
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n, k = 4, 2
    processed = signal_times(times, n, k)
    if processed == -1:
        print("Signal doesn't reach all nodes")
    else:
        print(f"The signal can be processed in: {processed} units")

    # Test 2
    times = [[1, 2, 1]]
    n, k = 2, 1
    processed = signal_times(times, n, k)
    if processed == -1:
        print("Signal doesn't reach all nodes")
    else:
        print(f"The signal can be processed in: {processed} units")

    # Test 3
    times = [[1, 2, 1]]
    n, k = 2, 2
    processed = signal_times(times, n, k)
    if processed == -1:
        print("Signal doesn't reach all nodes")
    else:
        print(f"The signal can be processed in: {processed} units")


if __name__ == "__main__":
    tests()
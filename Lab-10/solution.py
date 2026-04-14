import collections


def remove_stones(stones):
    # Mapping rows and columns to stone indices [cite: 50]
    graph = collections.defaultdict(list)
    for i, (x, y) in enumerate(stones):
        graph[x].append(i)
        graph[~y].append(i)  # Using ~y to differentiate column indices from rows

    visited = set()

    def dfs(stone_index):
        """Depth-first search to traverse connected stones."""
        visited.add(stone_index)
        x, y = stones[stone_index]
        for neighbor in graph[x] + graph[~y]:
            if neighbor not in visited:
                dfs(neighbor)

    components = 0
    n = len(stones)

    # Count how many separate "groups" of stones exist [cite: 51]
    for i in range(n):
        if i not in visited:
            components += 1
            dfs(i)

    # Max removed = Total - 1 stone left per component
    return n - components


# Quick test
if __name__ == "__main__":
    example_stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(f"Max stones removed: {remove_stones(example_stones)}")  # Output: 5
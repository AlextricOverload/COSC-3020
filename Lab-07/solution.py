#solution.py
# COSC 3020
# Lab Practice 7
# Alex Warren
# 2026-03-16

def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    # Use a set to keep track of all the rooms we have visited
    # Start by having visited room 0
    visited = {0}

    # Stack to keep track of the rooms we have keys for but haven't visited
    stack = [0]

    # While there are still rooms to explore in our stack
    while stack:
        current_room = stack.pop()

        # Go through all the keys found in the current room
        for key in rooms[current_room]:
            # If we find a key to a room we haven't visited yet
            if key not in visited:
                visited.add(key)  # mark as visited
                stack.append(key)  # Add it to the stack to explore its keys later

    # If the number of visited rooms equals the total number of rooms, we visited all the rooms
    return len(visited) == len(rooms)

def main():
    # Example 1 from the assignment
    rooms1 = [[1], [2], [3], []]
    result1 = can_visit_all_rooms(rooms1)
    print(f"Rooms: {rooms1}")
    print(f"Can visit all rooms: {result1}")  # Expected is true

    #Example 2 from the assignment
    rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
    result2 = can_visit_all_rooms(rooms2)
    print(f"Rooms: {rooms2}")
    print(f"Can visit all rooms: {result2}")  # Expected is false

if __name__ == "__main__":
    main()

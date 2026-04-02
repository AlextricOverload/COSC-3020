# Alex Warren
# COSC 3020
# Lab Practice 1
# 1-28-2026
# solution.py
# Contains the completed solution for the assignment
# Objective: Given an array of meeting time intervals, determine if a person could attend all meetings

from typing import List


# Main function
def main():
    # Get the intervals
    interval_list = get_intervals()
    # Check for overlap
    possible = check_intervals(interval_list)
    give_output(possible)


# Takes inputs and creates interval list
def get_intervals() -> List[list[int]]:
    interval_list = []
    number_of_meetings = int(input("How many meetings are on the schedule? "))  # How many intervals do we need?
    for _ in range(number_of_meetings):
        start_time = int(input("Enter when the meeting starts: "))  # Meeting start time
        end_time = int(input("Enter when the meeting ends: "))  # Meeting end time
        interval_list.append([start_time, end_time])  # Add interval to the list

    return interval_list


# Check the intervals for overlap
def check_intervals(interval_list: List[list[int]]) -> bool:
    # Sort intervals by their start times
    interval_list.sort(key=lambda x: x[0])

    for n in range(len(interval_list) - 1):
        current_end = interval_list[n][1]  # Time when the current meeting will end
        next_start = interval_list[n + 1][0]  # Time when the next meeting will start
        if current_end > next_start:  # The current meeting will overlap with the next one
            return False  # It is not possible to attend every meeting

    # If the program reaches the end of the for loop, no conflict exists
    return True


# Give output to user
def give_output(possible: bool):
    if possible:
        print("True!")
    else:
        print("False!")


# Call main
if __name__ == '__main__':
    main()

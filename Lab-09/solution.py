def wiggle_sort(nums):
    """
    Reorders the array in-place using a greedy swapping method.
    """
    for i in range(len(nums) - 1):
        # Even indices: current should be <= next [cite: 60]
        if i % 2 == 0:
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        # Odd indices: current should be >= next [cite: 60]
        else:
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

# Quick test
if __name__ == "__main__":
    example_nums = [3, 5, 2, 1, 6, 4]
    wiggle_sort(example_nums)
    print(f"Wiggle Sorted: {example_nums}") # e.g., [3, 5, 1, 6, 2, 4]
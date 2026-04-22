# the sorted array change the problem your two pointer approach to slowand fast pointer approach
# slow pointer moves one step at a time, fast pointer moves two steps at a time
# if there is a cycle, the fast pointer will eventually meet the slow pointer
# finding number of duplicate in a sorted array 
# For an input like nums = [1, 1, 2, 2, 3]
# first always unique 
def count_duplicates(nums):
    if not nums:
        return 0
    count = 1
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            count += 1
            slow += 1
            nums[slow] = nums[fast]
    print(nums)  # Print the unique elements
    return fast-1

print(count_duplicates([1, 1, 2, 2, 3]))  # Output: 3
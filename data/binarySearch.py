def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2    # middle index
        # your logic here
        # if nums[mid] == target → found it
        # if nums[mid] < target  → go right half
        # if nums[mid] > target  → go left half
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1   # not found

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))    # 3
print(binary_search(nums, 1))    # 0
print(binary_search(nums, 15))   # 7
print(binary_search(nums, 6))    # -1 not found
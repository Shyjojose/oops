def two_sum_sorted(nums, target):
    left= 0 
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

print(two_sum_sorted([1, 3, 5, 7, 9], 10))   # [1, 3] → indices [0, 4]? No — 1+9=10 → [0, 4]
print(two_sum_sorted([1, 3, 5, 7, 9], 8))    # 3+5=8 → [1, 2]
print(two_sum_sorted([1, 3, 5, 7, 9], 6))    # 1+5=6 → [0, 2]
def max_window_sum(nums, k):
    if k > len(nums):
        return None
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
  
    # slide across the rest
    # track the maximum
    # return it

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_window_sum([1, 4, 2, 9, 7, 3], 2))  # 16

# if k > len(nums):
#     return None              # ✅ edge case handled — window bigger than list

# window_sum = sum(nums[:k])   # ✅ first window calculated cleanly
# max_sum = window_sum         # ✅ starts max at first window

# for i in range(k, len(nums)):
#     window_sum += nums[i] - nums[i - k]   # ✅ slide — add new, drop old
#     max_sum = max(max_sum, window_sum)     # ✅ track maximum

# return max_sum               # ✅ clean return
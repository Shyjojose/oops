def merge(left, right):
    result = []
    i = 0   # pointer for left list
    j = 0   # pointer for right list

    # while both lists have items
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:           
            result.append(right[j])
            j += 1
        # compare front of each list
        # append the smaller one
        # move that pointer forward

    # one list may have leftovers — add them
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(nums):
    # base case — list of 1 or 0 items is already sorted
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])    # sort left half
    right = merge_sort(nums[mid:])   # sort right half
    return merge(left, right)        # merge them back

nums = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(nums))   # [3, 9, 10, 27, 38, 43, 82]
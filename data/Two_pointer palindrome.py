def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left = left + 1
            right -= 1
        else:
            return False
    return True

    # use two pointers
    # compare characters from both ends
    # if any pair doesn't match → return False
    # if pointers cross → return True

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("madam"))     # True
print(is_palindrome("python"))    # False
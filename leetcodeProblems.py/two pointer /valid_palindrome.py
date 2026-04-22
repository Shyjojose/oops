# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# # 1 <= s.length <= 2 * 105

def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at opposite ends
        left, right = 0, len(s) - 1
        
        while left < right:
            # 1. Skip non-alphanumeric from the left
            if not s[left].isalnum():
                left += 1
            # 2. Skip non-alphanumeric from the right
            elif not s[right].isalnum():
                right -= 1
            # 3. Compare valid characters (case-insensitive)
            else:
                if s[left].lower() != s[right].lower():
                    return False  # Early exit if a mismatch is found
                left += 1
                right -= 1
                
        return True  # If pointers meet, it's a palindrome

# 125. Valid Palindrome
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

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Filter and Reverse)
    # ---------------------------------------------------------
    def isPalindrome(self, s: str) -> bool:
        # 1. Create a new string with only alphanumeric chars, converted to lowercase
        # This uses extra memory to store 'clean_s'
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
        
        # 2. Check if the string equals its reverse
        return clean_s == clean_s[::-1]

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Two Pointers)
    # ---------------------------------------------------------
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 1. Move left pointer forward until we find an alphanumeric char
            if not s[left].isalnum():
                left += 1
                continue
            
            # 2. Move right pointer backward until we find an alphanumeric char
            if not s[right].isalnum():
                right -= 1
                continue
            
            # 3. Compare the characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # 4. If they match, move both pointers inward
            left += 1
            right -= 1
            
        return True

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach (Filter & Reverse)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate through the string once to build 'clean_s', 
    and once more to reverse it.
  
* Space Complexity: O(N)
  - Explanation: We create a new string 'clean_s' which can be as large 
    as the original input.
  - Verdict: Good, but we can save space.

2. Optimal Approach (Two Pointers)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We traverse the string from both ends, meeting in the middle. 
    Each character is visited at most once.
  
* Space Complexity: O(1)
  - Explanation: We only use two integer pointers (left, right). 
    No new strings or arrays are created.
  - Verdict: The standard interview solution (In-place).
"""

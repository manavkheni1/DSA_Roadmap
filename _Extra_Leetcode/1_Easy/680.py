# 680. Valid Palindrome II

# Easy

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Try deleting every char)
    # ⚠️ NOTE: This is O(N^2) and will Time Limit Exceed (TLE).
    # Included only for logic comparison.
    # ---------------------------------------------------------
    def validPalindromeBruteForce(self, s: str) -> bool:
        # Helper to check standard palindrome
        def check(sub):
            return sub == sub[::-1]
            
        # If it's already a palindrome, return True
        if check(s):
            return True
            
        # Try removing each character one by one
        for i in range(len(s)):
            # Create new string without character at index i
            temp = s[:i] + s[i+1:]
            if check(temp):
                return True
                
        return False

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Two Pointers + Greedy)
    # ---------------------------------------------------------
    def validPalindromeOptimal(self, s: str) -> bool:
        # Helper function: Checks if a specific range is a palindrome
        def is_palindrome_range(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Mismatch found! We have exactly ONE chance to delete.
                # We check two possibilities:
                # 1. Delete character at 'left' (check range left+1 to right)
                # 2. Delete character at 'right' (check range left to right-1)
                
                return (is_palindrome_range(s, left + 1, right) or 
                        is_palindrome_range(s, left, right - 1))
            
            # If match, move inward normally
            left += 1
            right -= 1
            
        return True

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force
--------------------------------------------
* Time Complexity:  O(N^2)
  - Explanation: Checking a palindrome takes O(N). We do this N times.
    For N=100,000, this is 10 billion operations (Too slow).
  
* Space Complexity: O(N)
  - Explanation: Creating the substring copies uses memory.

2. Optimal Approach (Two Pointers)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate the string once. If a mismatch occurs, 
    we iterate the remaining substring twice (constant work).
    Total operations ~ O(N).
  
* Space Complexity: O(1)
  - Explanation: We use standard pointers. 
    (Note: Recursion/Slicing might effectively use O(N) in Python internals, 
    but the algorithmic logic is O(1) extra space).
  - Verdict: Passes all test cases.
"""

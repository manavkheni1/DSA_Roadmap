# 344. Reverse String

# Easy

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.


class Solution:
    # ---------------------------------------------------------
    # Approach 1: Recursive (Conceptually simple, but uses Stack Space)
    # ---------------------------------------------------------
    def reverseStringRecursive(self, s: List[str]) -> None:
        def helper(left: int, right: int):
            if left >= right:
                return
            
            # Swap
            s[left], s[right] = s[right], s[left]
            
            # Recurse
            helper(left + 1, right - 1)
            
        helper(0, len(s) - 1)

    # ---------------------------------------------------------
    # Approach 2: Two Pointers (Optimal - Iterative)
    # ---------------------------------------------------------
    def reverseStringOptimal(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Swap characters at left and right
            # Python allows this in one line without a temp variable
            s[left], s[right] = s[right], s[left]
            
            # Move pointers inward
            left += 1
            right -= 1

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Recursive Approach
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We visit every element once (N/2 swaps).
  
* Space Complexity: O(N)
  - Explanation: The recursion stack grows to depth N/2. 
    This technically fails the "O(1) memory" constraint.

2. Optimal Approach (Two Pointers)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate through half the array.
  
* Space Complexity: O(1)
  - Explanation: We only use two integer variables (left, right).
    We modify the input list directly.
  - Verdict: The standard interview solution.
"""
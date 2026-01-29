# 263. Ugly Number

# Easy

# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Example 1:
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.

# Example 3:
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 
# Constraints:
# -231 <= n <= 231 - 1


class Solution:
    # ---------------------------------------------------------
    # Approach 1: Recursive (Clean & Mathematical)
    # ---------------------------------------------------------
    def isUglyRecursive(self, n: int) -> bool:
        # Edge Case: 0 or negative numbers are not ugly
        if n <= 0:
            return False
        
        # Base Case: If we reduce n down to 1, it is ugly.
        if n == 1:
            return True
        
        # Recursive Step: Try dividing by 2, 3, or 5
        if n % 2 == 0:
            return self.isUglyRecursive(n // 2)
        elif n % 3 == 0:
            return self.isUglyRecursive(n // 3)
        elif n % 5 == 0:
            return self.isUglyRecursive(n // 5)
            
        # If not divisible by 2, 3, or 5, and it's not 1, it has a bad prime factor.
        return False

    # ---------------------------------------------------------
    # Approach 2: Iterative (Optimal for standard use)
    # ---------------------------------------------------------
    def isUglyIterative(self, n: int) -> bool:
        # Edge cases
        if n <= 0:
            return False
            
        # Keep dividing n by 2, 3, and 5 as long as possible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n = n // factor
        
        # If the number is ugly, we should be left with 1.
        # Example: 6 -> (div by 2) -> 3 -> (div by 3) -> 1 => True
        # Example: 14 -> (div by 2) -> 7 -> (not div by 3 or 5) -> 7 => False
        return n == 1

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Recursive Approach
--------------------------------------------
* Time Complexity:  O(log N)
  - Explanation: We divide N by 2, 3, or 5 in each step. 
    This reduces the number logarithmically.
  
* Space Complexity: O(log N)
  - Explanation: The recursion stack can grow up to the number of divisions.

2. Iterative Approach (Recommended)
--------------------------------------------
* Time Complexity:  O(log N)
  - Explanation: Same logic, we just use a loop instead of function calls.
  
* Space Complexity: O(1)
  - Explanation: We use constant extra space.
  - Verdict: Best for interviews (No recursion depth limit issues).
"""
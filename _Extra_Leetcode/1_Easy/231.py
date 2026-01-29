# 231. Power of Two

# Easy

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: n = 3
# Output: false
 
# Constraints:
# -231 <= n <= 231 - 1

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Recursive (Standard Logic)
    # ---------------------------------------------------------
    def isPowerOfTwoRecursive(self, n: int) -> bool:
        # Base Case 1: If n becomes 1, it started as a power of two.
        if n == 1:
            return True
        
        # Base Case 2: If n becomes odd (and isn't 1) or is 0, it fails.
        if n <= 0 or n % 2 != 0:
            return False
            
        # Recursive Step: Keep dividing by 2
        return self.isPowerOfTwoRecursive(n // 2)

    # ---------------------------------------------------------
    # Approach 2: Bit Manipulation (True Optimal)
    # ---------------------------------------------------------
    def isPowerOfTwoBitwise(self, n: int) -> bool:
        # A power of two in binary always has exactly ONE '1' bit.
        # Example: 4 -> 100, 8 -> 1000, 16 -> 10000
        
        # Trick: If we subtract 1, all bits flip after the first '1'.
        # 4 (100) - 1 = 3 (011)
        # 4 & 3   = 100 & 011 = 000 (0)
        
        # So, n & (n-1) will always be 0 for powers of two.
        if n <= 0:
            return False
            
        return (n & (n - 1)) == 0

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Recursive Approach
--------------------------------------------
* Time Complexity:  O(log N)
  - Explanation: We divide the number by 2 in each step.
  
* Space Complexity: O(log N)
  - Explanation: Recursive stack depth.

2. Bit Manipulation (Optimal)
--------------------------------------------
* Time Complexity:  O(1)
  - Explanation: It's just one CPU operation. Instant.
  
* Space Complexity: O(1)
  - Explanation: No extra memory.
  - Verdict: The "Senior Engineer" solution.
"""
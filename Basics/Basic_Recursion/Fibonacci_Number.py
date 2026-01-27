# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
    
# Given n, calculate F(n).

 
# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Constraints:
# 0 <= n <= 30

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Standard Recursion)
    # ---------------------------------------------------------
    def fibBruteForce(self, n: int) -> int:
        # Base Case: F(0) = 0, F(1) = 1
        if n <= 1:
            return n
            
        # Recursive Step: F(n) = F(n-1) + F(n-2)
        return self.fibBruteForce(n - 1) + self.fibBruteForce(n - 2)

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Iterative / Bottom-Up)
    # ---------------------------------------------------------
    def fibOptimal(self, n: int) -> int:
        if n <= 1:
            return n
            
        # We only need the last two numbers to calculate the next one.
        # prev2 = F(i-2), prev1 = F(i-1)
        prev2 = 0
        prev1 = 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach (Recursion)
--------------------------------------------
* Time Complexity:  O(2^n)  (Exponential)
  - Explanation: Each call branches into two new calls. 
    For n=30, this executes ~800,000 steps. For n=50, it would take years.
  
* Space Complexity: O(n)
  - Explanation: The recursion stack goes 'n' deep.
  - Verdict: Terrible for large N. (Try running it with n=40 and watch it freeze).

2. Optimal Approach (Iterative)
--------------------------------------------
* Time Complexity:  O(n)
  - Explanation: We calculate each number exactly once in a simple loop.
  
* Space Complexity: O(1)
  - Explanation: We only store two variables (prev1, prev2) at any time.
  - Verdict: The standard efficient solution.
"""
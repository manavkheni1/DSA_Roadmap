# 70. Climbing Stairs

# Easy

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 
# Constraints:
# 1 <= n <= 45

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Recursion)
    # ---------------------------------------------------------
    def climbStairsRecursive(self, n: int) -> int:
        # Base Cases
        if n == 0 or n == 1:
            return 1
            
        # Recursive Step: Sum of ways to get to (n-1) and (n-2)
        return self.climbStairsRecursive(n - 1) + self.climbStairsRecursive(n - 2)

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Iterative / DP)
    # ---------------------------------------------------------
    def climbStairsOptimal(self, n: int) -> int:
        # Base Case: If 0 or 1 steps, there is only 1 way.
        if n <= 1:
            return 1
        
        # We only need the last two values (just like Fibonacci)
        prev2 = 1  # Ways to reach step 0
        prev1 = 1  # Ways to reach step 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Recursive Approach
--------------------------------------------
* Time Complexity:  O(2^N)
  - Explanation: Just like unoptimized Fibonacci, the recursion tree doubles 
    at every step. It is extremely slow for N > 30.
  
* Space Complexity: O(N)
  - Explanation: Stack depth proportional to N.

2. Optimal Approach (Iterative)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We loop from 2 to N exactly once.
  
* Space Complexity: O(1)
  - Explanation: We only use two variables (prev1, prev2) regardless of N.
  - Verdict: Best for interviews.
"""
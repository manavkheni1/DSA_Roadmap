# Factorial of a given number

# You are given an integer n. Return the value of n! or n factorial.
# Factorial of a number is the product of all positive integers less than or equal to that number.


# Example 1
# Input: n = 2
# Output: 2
# Explanation: 2! = 1 * 2 = 2.

# Example 2
# Input: n = 0
# Output: 1
# Explanation: 0! is defined as 1.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Iterative Solution (Optimal for Memory)
    # ---------------------------------------------------------
    def factorialIterative(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
            
        ans = 1
        # Loop from 2 up to n (inclusive)
        for i in range(2, n + 1):
            ans = ans * i
            
        return ans

    # ---------------------------------------------------------
    # Approach 2: Recursive Solution (Mathematical Definition)
    # ---------------------------------------------------------
    def factorialRecursive(self, n: int) -> int:
        # Base Case: Factorial of 0 or 1 is 1
        if n <= 1:
            return 1
            
        # Recursive Step: n! = n * (n-1)!
        return n * self.factorialRecursive(n - 1)

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Iterative Approach (factorialIterative)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: The loop runs from 2 to N.
  
* Space Complexity: O(1)
  - Explanation: We only use one variable 'ans' to store the product.
  - Verdict: Best for production code (Prevents Stack Overflow).

2. Recursive Approach (factorialRecursive)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: The function calls itself N times.
  
* Space Complexity: O(N)
  - Explanation: Each call adds a frame to the 'Stack Memory'.
    If N=10,000, this will crash (Stack Overflow) in Python.
  - Verdict: Elegant and simple, but expensive on memory.
"""
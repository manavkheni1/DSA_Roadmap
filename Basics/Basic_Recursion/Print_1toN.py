# Print 1 to N using Recursion

# Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.

# You must not use any loops such as for, while, or do-while.
# The function should print each number on a separate line, in increasing order from 1 to n.

# Example 1
# Input: n = 5
# Output:
# 1  
# 2  
# 3  
# 4  
# 5

# Example 2
# Input: n = 1
# Output:
# 1

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Iterative - Loop)
    # It is included here only for logic comparison.
    # ---------------------------------------------------------
    def printNo(self, n: int):
        # Simply iterate from 1 to N and print
        for i in range(1, n + 1):
            print(i)

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Recursion - Backtracking)
    # ---------------------------------------------------------
    def printNo(self, n: int):
        # Base Case: When n reaches 0, stop.
        if n == 0:
            return
        
        # Recursive Step:
        # 1. Call the function for (n - 1) FIRST.
        #    This pauses the current function and goes deeper until n=0.
        self.printNo(n - 1)
        
        # 2. Print n AFTER the recursive call returns.
        #    This ensures numbers are printed on the way "back" (1, then 2, then 3...)
        print(n)

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Iterative Approach (Loop)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: The loop runs N times.
  
* Space Complexity: O(1)
  - Explanation: No extra memory or stack space is used.
  - Verdict: Efficient, but violates the "No Loop" constraint.

2. Recursive Approach (Backtracking)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: The function is called recursively N times.
  
* Space Complexity: O(N)
  - Explanation: Recursion uses the "Stack" memory. 
    If N=100, we have 100 function calls waiting in the stack.
  - Verdict: The required solution for this specific problem.
"""
# Sum of First N Numbers

# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

# Example 1
# Input : N = 4
# Output : 10
# Explanation : first four natural numbers are 1, 2, 3, 4.
# Sum is 1 + 2 + 3 + 4 => 10.

# Example 2
# Input : N = 2
# Output : 3
# Explanation : first two natural numbers are 1, 2.
# Sum is 1 + 2 => 3.



class Solution:
    # ---------------------------------------------------------
    # Approach 1: Mathematical Formula (True Optimal in Real World)
    # ---------------------------------------------------------
    def sumOfSeriesFormula(self, n: int) -> int:
        # Standard formula for sum of first N natural numbers:
        # Sum = n * (n + 1) / 2
        return (n * (n + 1)) // 2

    # ---------------------------------------------------------
    # Approach 2: Recursive Solution (Required for Practice)
    # ---------------------------------------------------------
    def sumOfSeriesRecursive(self, n: int) -> int:
        # Base Case: When n is 0, the sum is 0.
        if n == 0:
            return 0
        
        # Recursive Step:
        # The sum of N numbers is N + (Sum of N-1 numbers)
        return n + self.sumOfSeriesRecursive(n - 1)

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Mathematical Formula (sumOfSeriesFormula)
--------------------------------------------
* Time Complexity:  O(1)
  - Explanation: Just one multiplication and one division. Instant.
  
* Space Complexity: O(1)
  - Explanation: No extra memory used.
  - Verdict: Best for performance, but skips the recursive lesson.

2. Recursive Approach (sumOfSeriesRecursive)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: The function calls itself N times (from N down to 0).
  
* Space Complexity: O(N)
  - Explanation: Each function call takes up space in the 'Stack Memory'.
    If N=1000, we use memory for 1000 calls.
  - Verdict: Good for learning, but risks 'Stack Overflow' for very large N.
"""
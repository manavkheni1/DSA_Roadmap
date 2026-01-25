# Divisors of a Number

# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called it's divisor.


# Example 1
# Input: n = 6
# Output = [1, 2, 3, 6]
# Explanation: The divisors of 6 are 1, 2, 3, 6.

# Example 2
# Input: n = 8
# Output: [1, 2, 4, 8]
# Explanation: The divisors of 8 are 1, 2, 4, 8.

import math

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Iterate all numbers)
    # ---------------------------------------------------------
    def printDivisors(self, n: int) -> list[int]:
        divisors = []
        # Iterate from 1 all the way up to n
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Square Root Method)
    # ---------------------------------------------------------
    def printDivisors(self, n: int) -> list[int]:
        divisors = []
        
        # We only need to iterate up to the square root of n.
        # Example: n=36. Sqrt(36)=6.
        # If we find 4 divides 36, we automatically know 9 (36/4) also divides it.
        sqrt_n = int(math.sqrt(n))
        
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                divisors.append(i)
                
                # If i is a divisor, then (n // i) is also a divisor.
                # We check (i != n // i) to avoid adding the square root twice 
                # (e.g., for n=36, don't add 6 twice).
                if i != n // i:
                    divisors.append(n // i)
        
        # The pairs are added in an unordered way (e.g., 1, 36, 2, 18...), 
        # so we must sort them at the end.
        divisors.sort()
        return divisors

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach
--------------------------------------------
* Time Complexity:  O(n)
  - Explanation: The loop runs exactly 'n' times. 
    If n = 10^9, this will take ~1 second (too slow for many competitive problems).
  
* Space Complexity: O(1)
  - Explanation: Ignoring the output list, we use no extra space.

2. Optimal Approach (Square Root)
--------------------------------------------
* Time Complexity:  O(sqrt(n))
  - Explanation: We only check numbers up to sqrt(n). 
    If n = 10^9, we only run ~31,622 iterations. This is massively faster.
    (Note: Sorting takes O(k log k) where k is the number of divisors, 
    but since k is very small compared to n, O(sqrt(n)) dominates).
  
* Space Complexity: O(1)
  - Explanation: We store divisors in the output list only. No intermediate data structures.
  - Verdict: The standard interview solution.
"""
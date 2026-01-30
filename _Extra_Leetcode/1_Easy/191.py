# 191. Number of 1 Bits

# Easy

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# Constraints:
# 1 <= n <= 231 - 1

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Loop and Shift (Check every bit)
    # ---------------------------------------------------------
    def hammingWeightLoop(self, n: int) -> int:
        count = 0
        while n > 0:
            # Check if the last bit is 1
            if n % 2 == 1:
                count += 1
            
            # Shift n to the right by 1 (divide by 2)
            n = n >> 1  # or n = n // 2
            
        return count

    # ---------------------------------------------------------
    # Approach 2: Brian Kernighan’s Algorithm (Optimal)
    # ---------------------------------------------------------
    def hammingWeightOptimal(self, n: int) -> int:
        # Trick: n & (n - 1) removes the rightmost '1' bit.
        # instead of checking 32 times, we only loop exactly as many times
        # as there are 1s.
        
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
            
        return count

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Loop and Shift
--------------------------------------------
* Time Complexity:  O(32) -> O(1)
  - Explanation: The loop runs once for every bit. Integers are 32-bit.
  
* Space Complexity: O(1)

2. Optimal Approach (n & n-1)
--------------------------------------------
* Time Complexity:  O(k) -> O(1)
  - Explanation: The loop runs 'k' times, where 'k' is the number of 1s.
    If n has only one '1' (e.g., 100000), this loop runs only once!
  
* Space Complexity: O(1)
  - Verdict: The fastest way to count bits.
"""
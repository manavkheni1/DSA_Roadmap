# Check for Prime Number

# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.


# Example 1
# Input: n = 5
# Output: true
# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# Example 2
# Input: n = 8
# Output: false
# Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

import math

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Check all numbers < n)
    # ---------------------------------------------------------
    def isPrime(self, n: int) -> bool:
        # 1. Edge case: numbers less than or equal to 1 are not prime
        if n <= 1:
            return False
        
        # 2. Iterate from 2 up to n-1
        for i in range(2, n):
            # If n is divisible by any number in this range, it's not prime
            if n % i == 0:
                return False
                
        # 3. If no divisors were found, it is prime
        return True

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Square Root Method)
    # ---------------------------------------------------------
    def isPrimeOptimal(self, n: int) -> bool:
        # 1. Edge case: numbers <= 1 are not prime
        if n <= 1:
            return False
            
        # 2. We only need to check up to sqrt(n).
        # Example: n=36. If 4 divides 36, then 9 also divides 36.
        # One factor is always <= sqrt(n) and the other is >= sqrt(n).
        # If we don't find a factor by sqrt(n), one doesn't exist.
        limit = int(math.sqrt(n))
        
        for i in range(2, limit + 1):
            if n % i == 0:
                return False
                
        return True


"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach
--------------------------------------------
* Time Complexity:  O(n)
  - Explanation: In the worst case (if n is a prime number), 
    the loop runs from 2 to n-1. For n = 10^9, this takes ~1 second.
  
* Space Complexity: O(1)
  - Explanation: We check numbers on the fly. No extra storage.

2. Optimal Approach (Square Root)
--------------------------------------------
* Time Complexity:  O(sqrt(n))
  - Explanation: We only check divisors up to the square root.
    For n = 10^9, sqrt(n) is ~31,622. This is instant.
  
* Space Complexity: O(1)
  - Explanation: Constant space usage.
  - Verdict: The standard, efficient way to check primality.
"""
# 204. Count Primes

# Given an integer n, return the number of prime numbers that are strictly less than n.


# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0
 
# Constraints:
# 0 <= n <= 5 * 106

import math

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force 
    # ---------------------------------------------------------
    def countPrimesBruteForce(self, n: int) -> int:
        if n <= 2: return 0
        
        count = 0
        # Check every number strictly less than n
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count
    
    # Helper to check primality
    def isPrime(self, num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # ---------------------------------------------------------
    # Approach 2: Sieve of Eratosthenes (Optimal)
    # ---------------------------------------------------------
    def countPrimesOptimal(self, n: int) -> int:
        # Edge case: No primes less than 2
        if n <= 2:
            return 0
            
        # 1. Initialize a boolean array "isPrime" of size n
        # Assume all are True initially. 0 and 1 are False.
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        
        # 2. Iterate from 2 up to sqrt(n)
        # We only need to sieve up to sqrt(n) because any non-prime  greater than sqrt(n) would have been marked by a smaller factor.
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                # If i is prime, mark all its multiples as False
                # Start marking from i*i because smaller multiples (like 2*i)  would have been marked by previous primes (like 2).
                # Step size is i.
                for multiple in range(i * i, n, i):
                    isPrime[multiple] = False
                    
        # 3. Count how many True values remain
        return sum(isPrime)

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach
--------------------------------------------
* Time Complexity:  O(n * sqrt(n))
  - Explanation: We iterate 'n' numbers, and for each number, we do a check 
    that takes sqrt(n). For n = 5,000,000, this is ~10^10 operations (Too slow).
  
* Space Complexity: O(1)
  - Explanation: No extra arrays used.

2. Optimal Approach (Sieve of Eratosthenes)
--------------------------------------------
* Time Complexity:  O(n * log(log(n)))
  - Explanation: This is a known harmonic series bound for the Sieve.
    It is nearly linear time and passes the 5*10^6 constraint easily.
  
* Space Complexity: O(n)
  - Explanation: We allocate a boolean array of size 'n'. 
    For n=5,000,000, this takes ~5MB of memory, which is acceptable.
  - Verdict: The standard solution for counting primes in a range.
"""
# GCD of Two Numbers

# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


# Example 1
# Input: n1 = 4, n2 = 6
# Output: 2
# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
# Greatest Common divisor = 2.

# Example 2
# Input: n1 = 9, n2 = 8
# Output: 1
# Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
# Greatest Common divisor = 1.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Iterate and Check)
    # ---------------------------------------------------------
    def gcd(self, n1: int, n2: int) -> int:
        # Initialize gcd to 1 (since 1 divides every number)
        gcd = 1
        
        # Iterate from 1 up to the smaller of the two numbers
        # We only need to check up to min(n1, n2) because a common divisor 
        # cannot be larger than the smallest number.
        for i in range(1, min(n1, n2) + 1):
            # Check if i divides both numbers exactly
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
                
        return gcd

    # ---------------------------------------------------------
    # Approach 2: Euclidean Algorithm (Optimal)
    # ---------------------------------------------------------
    def gcd(self, n1: int, n2: int) -> int:
        # Euclidean algorithm logic: gcd(a, b) = gcd(b, a % b)
        # We keep swapping n2 into n1, and the remainder into n2 until n2 is 0.
        while n2 > 0:
            n1, n2 = n2, n1 % n2
            
        # When n2 becomes 0, n1 holds the greatest common divisor
        return n1

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach (gcdBruteForce)
--------------------------------------------
* Time Complexity:  O(min(n1, n2))
  - Explanation: The loop runs from 1 to min(n1, n2). In the worst case 
    (e.g., large prime numbers), it checks every integer up to that limit.
  
* Space Complexity: O(1)
  - Explanation: Only a single variable 'gcd' is used.
  - Verdict: Too slow for large inputs (e.g., n = 10^9).

2. Euclidean Algorithm (gcdOptimal)
--------------------------------------------
* Time Complexity:  O(log(min(n1, n2)))
  - Explanation: In every step, the number is reduced significantly (at least by half).
    This is extremely fast even for very large numbers.
  
* Space Complexity: O(1)
  - Explanation: We use an iterative approach with no extra memory or recursion stack.
  - Verdict: The standard industry solution.
"""
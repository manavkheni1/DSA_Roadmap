# 50. Pow(x, n)

# Medium

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
# Constraints:
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Iterative Multiply)
    # ⚠️ NOTE: This results in Time Limit Exceeded (TLE) for large n.
    # Included only for logic comparison.
    # ---------------------------------------------------------
    def myPowBruteForce(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        # Handle negative exponent: x^-n = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        for _ in range(n):
            ans = ans * x
            
        return ans

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Binary Exponentiation)
    # ---------------------------------------------------------
    def myPowOptimal(self, x: float, n: int) -> float:
        # Edge Case: Anything to the power of 0 is 1
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        # x^-n is the same as (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1.0
        current_product = x
        
        # While we still have power left to calculate
        while n > 0:
            # If n is odd, multiply the result by the current product
            if n % 2 == 1:
                ans = ans * current_product
            
            # Square the base (x^2, x^4, x^8...)
            current_product = current_product * current_product
            
            # Divide n by 2 (move to the next bit)
            n = n // 2
            
        return ans

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: If N = 2 billion, we loop 2 billion times. 
    This will timeout instantly.
  
* Space Complexity: O(1)

2. Optimal Approach (Binary Exponentiation)
--------------------------------------------
* Time Complexity:  O(log N)
  - Explanation: We divide N by 2 in every step. 
    For N = 2 billion, it only takes about 31 steps.
  
* Space Complexity: O(1)
  - Explanation: We only use a few variables.
  - Verdict: The standard algorithm for cryptographic math.
"""
# 1281. Subtract the Product and Sum of Digits of an Integer

# Easy

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
# Example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# Example 2:
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 
# Constraints:
# 1 <= n <= 10^5

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (String Conversion)
    # ---------------------------------------------------------
    def subtractProductAndSum(self, n: int) -> int:
        # Convert number to string to iterate easily
        s = str(n)
        
        prod = 1
        summ = 0
        
        for char in s:
            digit = int(char)
            prod *= digit
            summ += digit
            
        return prod - summ

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Mathematical Extraction)
    # ---------------------------------------------------------
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0
        
        while n > 0:
            # 1. Get the last digit
            digit = n % 10
            
            # 2. Update accumulators
            product_of_digits *= digit
            sum_of_digits += digit
            
            # 3. Remove the last digit
            n = n // 10
            
        return product_of_digits - sum_of_digits

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force (String Conversion)
--------------------------------------------
* Time Complexity:  O(log10(N))
  - Explanation: The number of digits 'd' is log10(N). We iterate 'd' times.
  
* Space Complexity: O(log10(N))
  - Explanation: Converting an integer to a string creates a new string object 
    proportional to the number of digits.

2. Optimal Approach (Math)
--------------------------------------------
* Time Complexity:  O(log10(N))
  - Explanation: We loop once per digit. For N=234, loop runs 3 times.
  
* Space Complexity: O(1)
  - Explanation: We only use fixed integer variables (prod, sum, digit).
    No extra memory is allocated for string conversion.
  - Verdict: Best for memory efficiency.
"""

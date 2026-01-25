# Check if the Number is Armstrong

# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

# Example 1
# Input: n = 153
# Output: true
# Explanation: Number of digits : 3.
# 13 + 53 + 33 = 1 + 125 + 27 = 153.
# Therefore, it is an Armstrong number.

# Example 2
# Input: n = 12
# Output: false
# Explanation: Number of digits : 2.
# 12 + 22 = 1 + 4 = 5.
# Therefore, it is not an Armstrong number.

import math

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (String Conversion)
    # ---------------------------------------------------------
    def isArmstrong(self, n: int) -> bool:
        # Convert number to string to easily iterate digits
        s = str(n)
        k = len(s)
        
        # Calculate sum of digits raised to the power of k
        sum_power = 0
        for char in s:
            digit = int(char)
            sum_power += digit ** k
            
        return sum_power == n

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Mathematical)
    # ---------------------------------------------------------
    def isArmstrong(self, n: int) -> bool:
        if n == 0: return True
        
        # 1. Count digits without string conversion
        # math.log10(n) gives the power of 10. Floor + 1 gives digit count.
        k = math.floor(math.log10(n)) + 1
        
        # 2. Extract digits mathematically
        original_n = n
        sum_power = 0
        
        while n > 0:
            digit = n % 10          # Get last digit
            sum_power += digit ** k # Add digit^k to sum
            n = n // 10             # Remove last digit
            
        return sum_power == original_n

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach (String Conversion)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: Iterating through the string takes time proportional 
    to the number of digits.
  
* Space Complexity: O(log10(n))
  - Explanation: Creating a string requires converting and storing every digit 
    in memory. For a number with D digits, we use O(D) space.
  - Verdict: Simple to write, but wastes space.

2. Optimal Approach (Mathematical)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: We iterate through the digits once mathematically. 
    The time is the same order as brute force, but the operations are faster.
  
* Space Complexity: O(1)
  - Explanation: We only use integer variables (k, sum_power, digit). 
    No extra data structures are created.
  - Verdict: Best for interviews (Demonstrates space optimization).
"""
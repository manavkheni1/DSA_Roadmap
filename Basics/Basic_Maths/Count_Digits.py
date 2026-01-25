# Count all Digits of a Number

# You are given an integer n. You need to return the number of digits in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

# Example 1
# Input: n = 4
# Output: 1
# Explanation: There is only 1 digit in 4.

# Example 2
# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.

# Example 3
# Input: n = 234
# Output:
# 3

# Constraints
# 0 <= n <= 5000
# n will contain no leading zeroes except when it is 0 itself.

import math

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Mathematical Iteration (Optimal)
    # ---------------------------------------------------------
    def countDigitsMath(self, n: int) -> int:
        if n == 0: return 1  # Edge case: 0 has 1 digit
        
        n = abs(n)
        count = 0
        
        while n > 0:
            n = n // 10  # Remove the last digit
            count += 1
            
        return count

    # ---------------------------------------------------------
    # Approach 2: String Conversion 
    # ---------------------------------------------------------
    def countDigitsString(self, n: int) -> int:
        n_abs = abs(n)
        n_str = str(n_abs)
        return len(n_str)

    # ---------------------------------------------------------
    # Approach 3: Logarithmic Shortcut 
    # ---------------------------------------------------------
    def countDigitsLog(self, n: int) -> int:
        if n == 0: return 1
        return math.floor(math.log10(abs(n))) + 1

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Mathematical Approach (countDigitsMath)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: The loop runs once for every digit. A number 'n' 
    has roughly log10(n) digits.
  
* Space Complexity: O(1)
  - Explanation: We only use a counter variable. No extra memory 
    is allocated based on the size of the number.
  - Verdict: Best for interviews (Shows logic without extra space).

2. String Approach (countDigitsString)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: Converting int to string requires iterating over every digit.
  
* Space Complexity: O(log10(n))
  - Explanation: Creating the string requires memory proportional to 
    the number of digits (e.g., storing "12345" takes 5 chars).
  - Verdict: Cleanest to read, but uses extra memory.

3. Logarithmic Approach (countDigitsLog)
--------------------------------------------
* Time Complexity:  O(1) 
  - Explanation: Math operations are generally considered constant time
    for standard integer sizes.
  
* Space Complexity: O(1)
  - Explanation: Pure mathematical calculation.
  - Verdict: Fastest for competitive programming, but you must know the formula.
"""
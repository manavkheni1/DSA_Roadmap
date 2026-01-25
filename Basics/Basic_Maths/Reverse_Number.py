# Reverse a number

# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

# Example 1
# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.

# Example 2
# Input: n = 123
# Output: 321
# Explanation: Reverse of 123 is 321.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Mathematical Reversal (Optimal)
    # ---------------------------------------------------------
    def reverseMath(self, x: int) -> int:
        # 1. Check if the number is negative
        sign = -1 if x < 0 else 1
        
        # 2. Work with the positive version
        y = abs(x)
        revnum = 0
        
        while y > 0:
            lastdigit = y % 10
            revnum = (revnum * 10) + lastdigit
            y = y // 10
            
        # 3. Apply the sign back to the result
        return revnum * sign

    # ---------------------------------------------------------
    # Approach 2: String Conversion 
    # ---------------------------------------------------------
    def reverseString(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        # Convert to string, reverse slice, convert back to int
        rev = int(str(abs(x))[::-1])
        return rev * sign

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Mathematical Approach (reverseMath)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: The while loop processes one digit at a time. 
    The number of iterations equals the number of digits (approx log10(n)).
  
* Space Complexity: O(1)
  - Explanation: We only use fixed variables (sign, y, revnum) regardless 
    of the input size.
  - Verdict: Best for interviews (Demonstrates low-level logic).

2. String Approach (reverseString)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: Converting integer to string requires iterating over all digits. 
    Reversing the string takes another pass.
  
* Space Complexity: O(log10(n))
  - Explanation: Creating the string requires allocating memory proportional 
    to the number of digits.
  - Verdict: Concise, but higher space usage.
"""
# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Mathematical Reversal (Optimal Space)
    # ---------------------------------------------------------
    def isPalindromeMath(self, n: int) -> bool:
        if n < 0: return False  # Negative numbers are not palindromes
        
        copy = n
        revNum = 0

        while n > 0:
            lastDigit = n % 10
            revNum = (revNum * 10) + lastDigit
            n = n // 10
        
        return revNum == copy

    # ---------------------------------------------------------
    # Approach 2: String Conversion (Pythonic)
    # ---------------------------------------------------------
    def isPalindromeString(self, n: int) -> bool:
        s = str(n)
        return s == s[::-1]

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Mathematical Approach (isPalindromeMath)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: The while loop runs once for every digit in the number.
    A number 'n' has roughly log10(n) digits.
  
* Space Complexity: O(1)
  - Explanation: We only use a few variables (copy, revNum, lastDigit) 
    to store integers. No extra memory is allocated proportional to the input.
  - Verdict: Best for interviews (Shows logic without extra space).

2. String Approach (isPalindromeString)
--------------------------------------------
* Time Complexity:  O(log10(n))
  - Explanation: Converting int to string takes time proportional to the 
    number of digits. Reversing and comparing also takes O(digits).
  
* Space Complexity: O(log10(n))
  - Explanation: We create a string 's' that holds all digits. 
    If n has 100 digits, we need memory for 100 characters.
  - Verdict: Good for quick implementation, but uses extra memory.
"""
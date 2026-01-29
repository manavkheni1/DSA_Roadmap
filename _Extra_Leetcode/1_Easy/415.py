# 415. Add Strings

# Easy

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

# Constraints:
# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Type Casting)
    # ⚠️ NOTE: This is explicitly FORBIDDEN by the problem statement.
    # It is included only for logic comparison.
    # ---------------------------------------------------------
    def addStringsBruteForce(self, num1: str, num2: str) -> str:
        # Convert both strings to integers, add them, convert back.
        # Python handles arbitrarily large integers, so this works,
        # but in languages like C++/Java, this would overflow.
        return str(int(num1) + int(num2))

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Two Pointers / Elementary Math)
    # ---------------------------------------------------------
    def addStringsOptimal(self, num1: str, num2: str) -> str:
        res = []
        
        # Start pointers at the end of each string (least significant digit)
        i = len(num1) - 1
        j = len(num2) - 1
        
        carry = 0
        
        # Loop until we finish both strings AND handle any remaining carry
        while i >= 0 or j >= 0 or carry > 0:
            # Get the digit from num1 if available, else 0
            val1 = int(num1[i]) if i >= 0 else 0
            
            # Get the digit from num2 if available, else 0
            val2 = int(num2[j]) if j >= 0 else 0
            
            # 1. Sum the digits and the carry
            total = val1 + val2 + carry
            
            # 2. Update Carry (e.g., 15 // 10 = 1)
            carry = total // 10
            
            # 3. Add the last digit to result (e.g., 15 % 10 = 5)
            res.append(str(total % 10))
            
            # Move pointers to the left
            i -= 1
            j -= 1
        
        # The result is currently backwards (ones place first), so reverse it
        return "".join(res[::-1])

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force (Type Casting)
--------------------------------------------
* Time Complexity:  O(N + M)
  - Explanation: Converting string to int takes linear time based on length.
  
* Space Complexity: O(max(N, M))
  - Explanation: Storing the large integer result.
  - Verdict: Violates problem constraints ("Do not convert inputs directly").

2. Optimal Approach (Elementary Math)
--------------------------------------------
* Time Complexity:  O(max(N, M))
  - Explanation: We iterate through the longer string exactly once.
  
* Space Complexity: O(max(N, M))
  - Explanation: We build a result string that is roughly the size of the 
    largest input.
  - Verdict: The standard solution for Big Integer arithmetic.
"""
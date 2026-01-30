# 412. Fizz Buzz

# Easy

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 
# Constraints:
# 1 <= n <= 104

from typing import List

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Naive (Standard If-Else Chain)
    # ---------------------------------------------------------
    def fizzBuzzNaive(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            # Order matters! Check for 15 (3 and 5) first.
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        return result

    # ---------------------------------------------------------
    # Approach 2: String Concatenation (Cleaner & Extensible)
    # ---------------------------------------------------------
    def fizzBuzzOptimal(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            # Build the string parts
            current_str = ""
            
            if i % 3 == 0:
                current_str += "Fizz"
            if i % 5 == 0:
                current_str += "Buzz"
            
            # If string is empty, it means it's not divisible by 3 or 5
            if not current_str:
                current_str = str(i)
                
            result.append(current_str)
            
        return result

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Naive Approach
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate from 1 to N exactly once.
  
* Space Complexity: O(1)
  - Explanation: We don't use extra space (ignoring the output list).

2. String Concatenation Approach
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: Still just one loop.
  
* Space Complexity: O(1)
  - Verdict: This approach is better because it scales. 
    If we added a rule for "7 -> Jazz", we just add one 'if' statement 
    instead of rewriting the complicated 'if/else' chain.
"""
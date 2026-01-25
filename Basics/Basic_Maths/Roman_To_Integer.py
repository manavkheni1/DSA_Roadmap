# 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (String Replacement)
    # ---------------------------------------------------------
    def romanToInt(self, s: str) -> int:
        # The logic here is to replace the 6 subtraction instances with their additive equivalents. 
        # For example: "IV" (4) becomes "IIII" (1+1+1+1).
        # "IX" (9) becomes "VIIII" (5+1+1+1+1).
        translations = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC": "LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC"
        }

        # Replace all subtraction cases with additive ones
        for symbol, replacement in translations.items():
            s = s.replace(symbol, replacement)
            
        # Now we just sum up the values directly
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        
        for char in s:
            total += values[char]
            
        return total

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (One Pass Iteration)
    # ---------------------------------------------------------
    def romanToInt(self, s: str) -> int:
        # standard mapping
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current value is less than the next value, it means we have a subtraction case (e.g., IV -> 1 < 5).
            # We subtract the current value.
            # (i < n - 1) ensures we don't go out of bounds on the last character.
            if i < n - 1 and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                # Otherwise, just add it
                total += values[s[i]]
                
        return total

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach (String Replacement)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: Although replace() looks simple, it scans the string multiple 
    times. The final summation is also O(N).
  
* Space Complexity: O(N)
  - Explanation: String replacement creates a new string in memory, 
    potentially larger than the original input.

2. Optimal Approach (One Pass)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate through the string exactly once. 
    This is O(N) where N is the length of the string.
  
* Space Complexity: O(1)
  - Explanation: We only use a hash map of fixed size (7 symbols) 
    and a few integer variables. It uses constant extra space.
  - Verdict: Standard interview solution.
"""
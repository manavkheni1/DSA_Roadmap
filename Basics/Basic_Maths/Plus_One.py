# 66. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Type Casting)
    # ---------------------------------------------------------
    def plusOneBruteForce(self, digits: list[int]) -> list[int]:
        # 1. Convert list of ints to a single string: [1, 2, 3] -> "123"
        s = "".join(map(str, digits))
        
        # 2. Convert to integer and add one: 123 + 1 = 124
        num = int(s) + 1
        
        # 3. Convert back to string and then list of ints: 124 -> "124" -> [1, 2, 4]
        return [int(x) for x in str(num)]

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (School Addition Logic)
    # ---------------------------------------------------------
    def plusOneOptimal(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Iterate backwards from the last digit
        for i in range(n - 1, -1, -1):
            # If digit is less than 9, just add 1 and return immediately
            # Example: [1, 2, 3] -> 3 becomes 4 -> return [1, 2, 4]
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9, it becomes 0 and we continue the loop (carry over)
            # Example: [1, 2, 9] -> 9 becomes 0 -> loop continues to 2
            digits[i] = 0
            
        # If the loop finishes, it means ALL digits were 9s (e.g., [9, 9, 9] -> [0, 0, 0])
        # We need to add a leading 1.
        return [1] + digits

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach (Type Casting)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: Iterating the list to make a string takes O(N). 
    Converting back also takes O(N).
  
* Space Complexity: O(N)
  - Explanation: Converting to a string creates a new object in memory 
    proportional to the size of the input.

2. Optimal Approach (In-Place Array Modification)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: In the worst case (e.g., 999), we iterate through all digits once.
    In the best case (e.g., 123), it runs in O(1).
  
* Space Complexity: O(1)
  - Explanation: We modify the input array directly. 
    (Technically O(N) only if we need to resize for the [9,9] case, 
    but usually considered O(1) auxiliary space).
  - Verdict: Best for interviews (Shows logic without relying on BigInt libraries).
"""
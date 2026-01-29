# 268. Missing Number

# Easy

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Mathematical Formula (Sum Difference)
    # ---------------------------------------------------------
    def missingNumberMath(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Calculate Expected Sum of 0 to n: (n * (n+1)) / 2
        expected_sum = (n * (n + 1)) // 2
        
        # 2. Calculate Actual Sum of the array
        actual_sum = sum(nums)
        
        # 3. The difference is the missing number
        return expected_sum - actual_sum

    # ---------------------------------------------------------
    # Approach 2: Bit Manipulation (XOR) - Interview Favorite
    # ---------------------------------------------------------
    def missingNumberXOR(self, nums: list[int]) -> int:
        # XOR Logic: a ^ a = 0.
        # If we XOR all indices (0 to n) and all values in the array,
        # the duplicates cancel out, leaving only the missing number.
        
        n = len(nums)
        ans = 0
        
        # XOR all indices from 1 to n
        for i in range(1, n + 1):
            ans ^= i
            
        # XOR all values in the array
        for num in nums:
            ans ^= num
            
        return ans

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Mathematical Approach (Sum)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate the array once to calculate the sum().
  
* Space Complexity: O(1)
  - Explanation: We only use a few integer variables.
  - Verdict: Simple, clean, and efficient.

2. XOR Approach (Bit Manipulation)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate the array once.
  
* Space Complexity: O(1)
  - Explanation: No extra memory.
  - Verdict: Prevents Integer Overflow (important in languages like C++/Java).
"""
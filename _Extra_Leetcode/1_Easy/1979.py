# 1979. Find Greatest Common Divisor of Array

# Easy

# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Example 1:
# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

# Example 2:
# Input: nums = [7,5,6,8,3]
# Output: 1
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 8.
# The greatest common divisor of 3 and 8 is 1.

# Example 3:
# Input: nums = [3,3]
# Output: 3
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 3.
# The greatest common divisor of 3 and 3 is 3.
 
# Constraints:
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000


class Solution:
    # ---------------------------------------------------------
    # Approach 1: Brute Force (Linear Search for GCD)
    # ---------------------------------------------------------
    def findGCDBruteForce(self, nums: list[int]) -> int:
        # 1. Find the smallest and largest numbers manually
        min_val = float('inf')
        max_val = float('-inf')
        
        for num in nums:
            if num < min_val: min_val = num
            if num > max_val: max_val = num
            
        # 2. Find GCD by checking every number from min_val down to 1
        # The largest number that divides both is the GCD.
        for i in range(min_val, 0, -1):
            if min_val % i == 0 and max_val % i == 0:
                return i
        
        return 1  # Should never reach here since 1 always divides everything

    # ---------------------------------------------------------
    # Approach 2: Optimal Solution (Euclidean Algorithm)
    # ---------------------------------------------------------
    def findGCDOptimal(self, nums: list[int]) -> int:
        # Helper function for Euclidean Algorithm (Recursion)
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        # 1. Find min and max (Python's built-in functions are optimized C code)
        mn = min(nums)
        mx = max(nums)
        
        # 2. Calculate GCD of the two numbers
        return gcd(mx, mn)

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Brute Force Approach
--------------------------------------------
* Time Complexity:  O(N + min_val)
  - Explanation: O(N) to find min/max, plus O(min_val) to check divisors.
    If min_val is large (e.g., 1000), this is slower than Euclidean.
  
* Space Complexity: O(1)
  - Explanation: No extra memory.

2. Optimal Approach (Euclidean)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: 
    - Finding min/max takes O(N).
    - Calculating GCD takes O(log(min_val)).
    - Total = O(N + log(min)). Since N is usually larger, we say O(N).
  
* Space Complexity: O(log(min_val))
  - Explanation: Recursion stack for GCD. (Or O(1) if implemented iteratively).
  - Verdict: The standard efficient solution.
"""
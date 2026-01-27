# Reverse an array

# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

# Example 1
# Input: n=5, arr = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

# Example 2
# Input: n=6, arr = [1,2,1,1,5,1]
# Output: [1,5,1,1,2,1]
# Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

class Solution:
    # ---------------------------------------------------------
    # Approach 1: Iterative (Two Pointers) - Optimal for Space
    # ---------------------------------------------------------
    def reverseArrayIterative(self, arr: list[int]) -> list[int]:
        left = 0
        right = len(arr) - 1
        
        # Swap elements from both ends moving inwards
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        return arr

    # ---------------------------------------------------------
    # Approach 2: Recursive (Depth-First Swap)
    # ---------------------------------------------------------
    def reverseArrayRecursive(self, arr: list[int], start: int, end: int) -> list[int]:
        # Base Case: When pointers cross or meet, stop.
        if start >= end:
            return arr
            
        # Swap the current start and end
        arr[start], arr[end] = arr[end], arr[start]
        
        # Recurse: Move pointers inward
        return self.reverseArrayRecursive(arr, start + 1, end - 1)

"""
=========================================================
📊 COMPLEXITY ANALYSIS
=========================================================

1. Iterative Approach (Two Pointers)
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We iterate through half the array (N/2 swaps).
  
* Space Complexity: O(1)
  - Explanation: We reverse the array in-place without extra memory.
  - Verdict: Best for production code.

2. Recursive Approach
--------------------------------------------
* Time Complexity:  O(N)
  - Explanation: We make N/2 recursive calls.
  
* Space Complexity: O(N)
  - Explanation: Recursion uses 'Stack Memory'. 
    For a large array (e.g., 100,000 elements), this will crash (Stack Overflow).
  - Verdict: Good for learning, but Iterative is preferred here.
"""
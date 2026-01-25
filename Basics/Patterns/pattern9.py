# Pattern 9

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

#     * 
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

class Solution:
    def pattern9(self, n):
        # upper half
        for i in range(1, n + 1):
            # leading spaces
            print(" " * (n - i), end="")
            # stars
            print("*" * (2 * i - 1))

        # lower half
        for i in range(n, 0, -1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))

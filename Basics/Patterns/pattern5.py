# Pattern 5

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# ****
# ***
# **
# *

class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            print('*' * i)
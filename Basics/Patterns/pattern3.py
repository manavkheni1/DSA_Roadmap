# Pattern 3

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 1
# 12
# 123
# 1234
# 12345

class Solution:
    def pattern3(self, n):
        for i in range (1, n+1):
            for j in range(1, i+1):
                print(j ,end = "")
            print()
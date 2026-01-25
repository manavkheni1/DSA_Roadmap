# Pattern 8

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *********
#  *******
#   *****
#    ***
#     *

class Solution:
    def pattern8(self, n):
        for i in range (0,n):
            for j in range(0, i):
                print(' ', end="")
            for j in range(0, 2*n-(2*i+1)):
                print('*', end="")
            print()

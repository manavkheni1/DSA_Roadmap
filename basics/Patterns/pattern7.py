# Pattern 7

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

#     *
#    ***
#   *****
#  *******
# *********

class Solution:
    def pattern7(self, n):
        # Outer loop will run for rows.
        for i in range(0, n):
            #This loop will print the spaces
            for j in range(0, (n-i-1)):
                print(' ', end='')
            # This loop will print asterisk.
            for j in range(0, 2*i +1):
                print('*', end="")
            print()

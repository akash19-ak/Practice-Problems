# Program Name: Find Two Unique Numbers
# Purpose: Find two numbers that appear only once
# Author: Akash
# Inputs: List of integers
# Output: List with two unique numbers

class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        
        # Step 1: XOR all elements
        for num in nums:
            xor ^= num
        
        # Step 2: Find rightmost set bit
        diff = xor & -xor
        
        a = 0
        b = 0
        
        # Step 3: Divide into two groups and XOR
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
# Happy Number
# Purpose: Determine whether n is a happy number.
# Algorithm: Floyd's Cycle Detection

class Solution:
    def isHappy(self, n):
        def next_num(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1
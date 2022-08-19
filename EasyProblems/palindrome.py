'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #here we can define optionally some constraints
        num = str(x)
        return num==num[::-1]

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #create an empty dictionary
        h = {} 
        #iterate throuh the given list
        for i,num in enumerate(nums):
            complement = target-num
            #if complement is not in dictionary we added it
            if complement not in h:
                #key: number val, val: position
                h[num]=i
            #otherwhise... (in this case, use current index)
            else:
                return[h[complement],i]

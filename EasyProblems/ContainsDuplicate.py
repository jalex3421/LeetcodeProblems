'''
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if 1 <= len(nums) <= 10**5:
            return len(nums)!=len(set(nums))

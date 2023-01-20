'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two index to perform binary search
        l, h = 0, len(nums)-1
        while l<h: #loop while condition 
            m = (l + h)//2 #obtain middle point: main idea of binary search 
            #Case 1) middle point is equal to target
            if nums[m]==target:
                return m
            #Case 2) middle is bigger than target. Shrink h
            elif nums[m]>target:
                h = m - 1
            #Case 3) middle is lower than target. Increase l
            else:
                l = m + 1
        #In the case we have shrink the interval at maximum, and we are outside the loop
        #the only option to the target is being l. If its h, in the loop we have found that
        if nums[l]==target: 
            return l
        #otherwhise: the element simply is not there.Return -1
        return (-1)

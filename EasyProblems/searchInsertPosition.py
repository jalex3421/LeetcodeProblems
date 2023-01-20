'''
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. If not, return the index
    where it would be if it were inserted in order.
    The complexity should be o(logn)
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,h = 0,len(nums)
        while(l<h):
            m = (l+h)//2
            if nums[m] < target:
                l = m + 1
            else:
                h = m
        return l

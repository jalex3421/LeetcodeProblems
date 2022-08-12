'''
Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #define lower top and upper top
        l , r = 0, len(nums)-1
        while l <= r:
            #obtain mid value
            mid=int((l+r)/2)
            #First posibility: enlarge low top
            if nums[mid] < target:
                l = mid+1
            else:
                #in order to deal with duplicate values
                if nums[mid]== target and nums[mid-1]!=target:
                    return mid
                else:
                    r = mid-1
        return l

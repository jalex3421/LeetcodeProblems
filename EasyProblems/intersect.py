'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
 Each element in the result must appear as many times as it shows in both arrays 
 and you may return the result in any order.
'''


class Solution:
   def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Really important Counter collection: return number of apparences of certain term
        counts = collections.Counter(nums1)
        intersection = []
        #iterate through numbers in second list
        for num in nums2:
            #check wheter number of apparences is not zero
            if counts[num] > 0:
                intersection.append(num)
                #decrease one unit in order to make zero in future
                counts[num] -= 1
        return intersection
        

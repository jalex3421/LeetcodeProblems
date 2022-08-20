'''
ou are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
 two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored 
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first 
m elements denote the elements that should be merged, and the last n elements are set to 0
 and should be ignored. nums2 has a length of n.
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        
        #Start iterating over two arrays
        while m > 0 and n > 0:
            #case the biggest of nums1 is greater than nums2
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                #in the other case
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        #n is not zero
        if n > 0:
            nums1[:n] = nums2[:n]

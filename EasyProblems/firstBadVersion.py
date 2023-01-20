# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
#The domain of bad version: 1-n

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #Apply binary search in the interval. 
        l,h = 1,n
        while l < h:
            m = (l + h) // 2
            #we are planning to obtain the first bad version
            if isBadVersion(m):
                #That represent that we can shrink the interval
                h = m
            else:
                l = (m+1)
        return l 

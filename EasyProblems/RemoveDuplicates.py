class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
        #put numbers at the head of the array
        nums[:len(result)] = result
        return len(result)     

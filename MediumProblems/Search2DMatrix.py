'''
Write an efficient algorithm that searches for a value target in an 
m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        #1)If empty Matrix
        if not matrix or not matrix[0]: 
            return False
        
        #2)Otherwise, we apply binary search over a 'sorted array'
        rows,columns = len(matrix),len(matrix[0])
        #asign index in order to perform the search
        beginning, end = 0, columns*rows - 1
        
        while beginning < end:
            mid = (beginning + end)//2 #threat like a sorted array
            if matrix[mid//columns][mid%columns] < target:
                beginning = mid + 1
            else:
                end = mid        
        return (matrix[beginning//columns][beginning%columns] == target)

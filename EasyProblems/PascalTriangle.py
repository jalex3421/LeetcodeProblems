'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above.
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #initialize triangle
        triangle = [[1]]
        for r in range(1, numRows):
            #add new level of the triangle (current level)
            triangle.append([1] * (r+1)) 
            #traverse items in triangle
            for c in range(1, r):
                triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c] 
        return triangle
       

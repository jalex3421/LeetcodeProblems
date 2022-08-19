class Solution:
    def reverse(self, x: int) -> int:
  
        rev = int(str(abs(x))[::-1])
        
        return (-rev if x < 0 else rev) if -(2**31)-1 < rev < 2**31 else 0

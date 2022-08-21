'''
Given a string s, find the first non-repeating character in it and 
return its index. If it does not exist, return -1.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {} #create an empty dictionary
        
        #fill dictionary
        for character in s:
            if character not in d: 
                d[character] = 1
            else: 
                d[character] += 1
        
        #traverse given string
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
            
        return -1
    

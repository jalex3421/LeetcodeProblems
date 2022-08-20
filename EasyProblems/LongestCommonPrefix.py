'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''


class Solution:
    def longestCommonPrefix(self, m):
        #if empty list then return empty character
        if not m: 
            return ''
        #since list of string will be sorted and retrieved min max by alphebetic order
        m.sort()
        s1,s2= m[0],m[-1]
        print(s1)
        print(s2)
        
        for pos, char in enumerate(s1):
            #if character in s1 does not apper in s2
            if char != s2[pos]:
                return s1[:pos] #stop until hit the split index
        return s1

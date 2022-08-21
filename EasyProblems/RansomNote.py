'''
Given two strings ransomNote and magazine, return true if 
ransomNote can be constructed by using the letters from magazine 
and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #substract number of appearence of common elements...
        #Substraction operation!!
        return not len(Counter(ransomNote) - Counter(magazine))

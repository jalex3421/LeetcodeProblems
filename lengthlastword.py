'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #separte input string with blank spaces
        words = str.split(s," ")
        #remove blank spaces from list
        words = [x for x in words if x]
        #return length of last element
        return len(words[len(words)-1])

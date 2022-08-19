class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #check wheter the constrains work or not 
        #dictionary with stuff
        dictionary=  {'I':1 , 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #'translate' each term of string input
        a = [dictionary[i] for i in s]
        special_elements = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for i in range(len(a)-1):
			#check pairs of elements in order to find out if they are in special_elements list
            if s[i:i+2] in  special_elements:
                a[i] = -a[i] #change sign
        return sum(a) 

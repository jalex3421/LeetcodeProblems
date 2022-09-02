# ------------------ OBJECTIVE ---------------------------
# Check whether the given string has valid parentheses or not
#-----------------------------------------------------------

class Solution:
    def isValid(self, s):
        #define a stack: simple approach
        stack = [] 
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            #first thing to do
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                #break conditions:
                #1) wheather stack empty
                #2) not valid pair on top of the stack
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return (stack == [])
        
        

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket not in bracket_map: 
                # opening bracket
                stack.append(bracket)
            else: 
                # closing bracket
                if stack and stack[-1] == bracket_map[bracket]:
                    stack.pop()
                else:
                    return False

        return not stack 

# stack = []
# loop through s
#   if opening bracket --> add
#   elif closing bracker:
#       check if last one not null and last one is closing
#           pop from stack
#       else
#           return False
# return not stack 

# time - O(n)
# space - O(n)
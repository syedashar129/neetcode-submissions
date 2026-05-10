class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if stack and brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


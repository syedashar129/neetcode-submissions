class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops_stack = []
        for op in operations:
            if op == '+':
                ops_stack.append(ops_stack[-2] + ops_stack[-1])
            elif op == 'C': 
                ops_stack.pop()
            elif op == 'D':
                ops_stack.append(ops_stack[-1] * 2)
            else:
                ops_stack.append(int(op))
        return sum(ops_stack)
            
    


# ops_stack
# loop thorugh operations
#   if '+: --> 
#   elif 'C': add to stack (stack[-2] + stack[-1])
#   elif 'D': -->  add to stack (stack[-1] * 2)
#   else: --> add number to stack

# return stack

# time: O(n)
# space: O(n)
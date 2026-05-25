class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            sum_val = numbers[start] + numbers[end]
            # if sum equal
            if sum_val == target:
                return [start + 1, end + 1]
            # if sum greater 
            elif sum_val > target:
                end -= 1
            # if sum less
            elif sum_val < target:
                start += 1

# increasing order --> 2 pointer
# O(1)
# return indexes
# only 1 valid Solution --> array return
# there can be negative numbers
# minimum input is 2


# we are going to go with a 2 pointer appraoch here
# merging pointers 

# check if sum > target 
#   if true --> decrease end pointer 
#   else --> increase start pointer
#   if equal target --> return [start, end]

# time; O(n) --> most opt
# space: O(1) --> most opt
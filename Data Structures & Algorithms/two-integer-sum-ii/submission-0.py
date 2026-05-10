class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer = 0
        end_pointer = len(numbers) - 1

        # iterate
        while start_pointer < end_pointer:
            if numbers[start_pointer] + numbers[end_pointer] == target:
                return [start_pointer + 1, end_pointer + 1]
            elif numbers[start_pointer] + numbers[end_pointer] > target:
                end_pointer -= 1
            elif numbers[start_pointer] + numbers[end_pointer] < target:
                start_pointer += 1
        
            




# approach
# 2 pointer - merging 
# increasing order 


# start pointer 
# end pointer 

# iterate thorguh numberes
# if start value + end value = target
#   return [start pointer, end pointer]
# if start value + end value > target 
#   decrease end pointer by 1
# elif start value + end value < target:
#   increase start pointer by 1


# complexity 
# time - n --> O(n)
# space = 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap question 
        # key: value value: index (since we are returning the value)

        # iterate and create map
        # check duing iteration if any taget - any existing value == current
            # if so --> return existig value index first, current inedx second

        nums_map = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in nums_map:
                # found match --> return 
                first_index = nums_map[check]
                second_index = i
                return [first_index, second_index]
            else:
                # not found --> make map 
                nums_map[num] = i # todo: think abt duplicate num

        

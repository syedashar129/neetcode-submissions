class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}

        for i, num in enumerate(nums):
            # check
            if target - num in nums_hashmap:
                return [nums_hashmap[target-num], i]

            nums_hashmap[num] = i


# store values as key
# store index as values



# time: O(n)
# space: O(n)

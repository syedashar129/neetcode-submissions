class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap question
        # iterate + add + check
        # if any value is more than 1 --> return true
        # else false
        nums_map = {}
        for num in nums:
            # check if already there --> if yes add
            if num in nums_map:
                return True
            else:
                # not in map, add new entry
                nums_map[num] = 1
        return False

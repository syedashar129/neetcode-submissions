class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            target_num = target - num
            if target_num in seen:
                return [seen[target_num],index]
            
            # add to seen hashmap
            seen[num] = index

        return None

            


        
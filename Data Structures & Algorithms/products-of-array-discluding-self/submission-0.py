import math
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = nums.copy()

        for index, number in enumerate(nums):
            nums.pop(index)

            print(index)
            new_arr[index] = math.prod(nums)

            nums.insert(index, number)

        print(new_arr)
        return new_arr

        
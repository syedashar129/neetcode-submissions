class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        # do prefix 
        prefix_num = 1 # this is the one before first index
        for i in range(len(nums)):
            res[i] = prefix_num
            prefix_num *= nums[i] 

        # do post fix
        postfix_num = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix_num
            postfix_num *= nums[i]

        return res

    # this division is not allowed, we should add the sums of the left and right
    # iterate
    # create prefix sum
    # create postfix sum
    # iterate and multiply the prefix by the post fix





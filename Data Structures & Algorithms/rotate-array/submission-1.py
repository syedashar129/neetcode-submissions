class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k %= n

        # reverse 3 times 
        reverse(0, n - 1)  # revesre the array 
        reverse(0, k - 1) # reverse first half
        reverse(k, n - 1) # reverse second half 

        

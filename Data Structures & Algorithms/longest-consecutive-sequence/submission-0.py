class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        # check if number does no
        for num in nums_set:
            length = 0
            if num - 1 not in nums_set: # checking if start
                length+=1
            while (num + length) in nums_set:
                length+=1
            longest = max(length, longest)
        
        return longest

                
                

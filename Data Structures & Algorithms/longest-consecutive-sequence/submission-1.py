class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in nums_set:
                count = 1
                while (num + count) in nums_set:
                    count +=1
                longest = max(longest, count)
        return longest
    
    # bruet force solution here:
    # we could just sort into a set
    # count until whenmever it is not + 1

    # approach 
    # set to remove duplicates
    # find the first number in the seq
    # then find after that if length fro first one exisst in set
    # iterate until not longer exists
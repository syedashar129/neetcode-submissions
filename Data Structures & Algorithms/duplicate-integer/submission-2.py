class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# use set --> O(1)
# iterate through nums --> O(n)
    # add to set O(1)

# return set != nums



# time: O(n)
# space: O(1)

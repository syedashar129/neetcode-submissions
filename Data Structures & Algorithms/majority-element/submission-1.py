class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_element = 0

        for num in nums:
            if count == 0:
                majority_element = num
            
            count += (1 if num == majority_element else -1)
        
        return majority_element


# goal O(n) n O(1)
# time; o(n)
# space: O(1)

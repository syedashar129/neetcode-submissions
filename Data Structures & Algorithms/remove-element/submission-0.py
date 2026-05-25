class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []

        # build new list without the duplicate 
        for num in nums:
            if num != val:
                tmp.append(num)

        # set the main array into the tmp
        for i, num in enumerate(tmp):
            nums[i] = tmp[i]

        return len(tmp)

# brute force

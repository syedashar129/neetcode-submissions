class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index = m + n - 1

        # merge into nums1
        while m > 0 and n > 0:
            # if greater --> insert nums2 into nums1
            if nums2[n - 1] > nums1[m - 1]:
                nums1[last_index] = nums2[n - 1]
                n -= 1
            # else (smaller or equal) --> keep nums1 value in
            else:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            last_index -= 1
        
        # leftover
        while n > 0:
            nums1[last_index] = nums2[n - 1]
            n -= 1
            last_index -= 1


# 2 pointer appraoch 
# merge from tehe bac
# 
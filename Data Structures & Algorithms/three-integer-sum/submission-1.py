class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr = 0 
        last_index = len(nums) - 1

        final_arr = []
        while curr < last_index:
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr+=1
                continue
            left = curr + 1
            right = len(nums) - 1
            
            while left < right:
                num_sum = nums[curr] + nums[left] + nums[right]
                
                if num_sum > 0:
                    right -= 1
                elif num_sum < 0:
                    left += 1
                else:
                    final_arr.append([nums[curr],  nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

            curr += 1
        return final_arr


# time: O(nlogn) + O(n^2) = O(n^2)
# space: o(n)


# curr. left, right
# curr will start at index 0 
# left will be starting at index 1
# right will start at the end
# final_arr

# while curr < last index:
#   while left < right:
#       if sum > 0: --> move right pointer down 
#       elif sum < 0: --> move left pointer up
#       else: --> add [curr, right, left] into final_arr + move both pointers
#   curr +=

# return final_arr



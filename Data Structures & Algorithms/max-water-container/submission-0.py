class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            left_height, right_height = heights[l], heights[r]
            min_height = min(left_height, right_height)
            curr_max = min_height * (r - l)
            max_area = max(max_area, curr_max)


            if min_height == left_height:
                l += 1
            elif min_height == right_height:
                r -= 1

        return max_area
# width = index between
# height = value


# l, r = 0, len(heights) - 1
# max_area = 0
# while l < r:
#   left_height, right_height = heights[l], heights[r]
#   min_height = min(left_height, right_height)
#   curr_max = min_height * (r - l)
#   max_area = max(max_area, curr_max)

#   if min_height is left_height --> move left up 1
#   elif min hieght is right_height --> move right down 1
#   if equal --> move right down 1

# return max_area


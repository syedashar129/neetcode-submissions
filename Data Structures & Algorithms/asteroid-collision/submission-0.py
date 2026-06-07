class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            is_destroyed = False
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    is_destroyed = True
                    break
                else: # last > 
                    is_destroyed = True
                    break
            if not is_destroyed:
                stack.append(asteroid)
        
        return stack
                    


    
# index = position 
# absolute val = size
# sign = left/right

# smaller one explode at collision 
# if same --> both explode
# 2 ast moving same direction --> no collision


# loop through asteroid
#   collision while loop (last positive curr negative)
#       if last < abs(curr)
#           pop last
#       elif same
#           pop last
#           mark curr as detroyed
#           break
#       else
#           mark destroyed 
#           break
#   if not destroyed 
#       add to staack 

# time: O(n)
# space: O(n)
# 7 8 -9
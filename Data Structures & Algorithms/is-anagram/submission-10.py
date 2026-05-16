class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tracking_hashmap = defaultdict(int)

        # track if same on both 
        for i in range(len(s)):
            tracking_hashmap[s[i]] += 1
            tracking_hashmap[t[i]] -= 1

        for count in tracking_hashmap.values():
            if count != 0:
                return False
        
        return True

# 1. 2 hashmaps
# early pass if length dont match
# use hashmap and compare the frequency of each letter
# check hashmap1 == hashmap2

# 2. 1 hashmap
# use 1 hashmap and deelet from it 




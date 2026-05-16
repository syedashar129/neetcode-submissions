class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hashmap = defaultdict(int)
        t_hashmap = defaultdict(int)
        
        # build 1st hashhmap
        for letter in s:
            s_hashmap[letter] += 1

        # build 2nd hashmap 
        for letter in t:
            t_hashmap[letter] += 1

        return t_hashmap == s_hashmap


# 1. 2 hashmaps
# early pass if length dont match
# use hashmap and compare the frequency of each letter
# check hashmap1 == hashmap2

# 2. 1 hashmap
# use 1 hashmap and deelet from it 




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if size is off --> return false
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        
        # iterate through each one seperately
        for letter in s:
            s_map[letter] = s_map.get(letter, 0) + 1

        for letter in t:
            t_map[letter] = t_map.get(letter, 0) + 1

        # check if both dicts are the same
        return s_map == t_map
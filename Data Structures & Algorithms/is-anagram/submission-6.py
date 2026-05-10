class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        print(f'sorted s : {sorted_s}')
        print(f'sorted t : {sorted_t}')

        for index, letter in enumerate(sorted_s):
            if sorted_t[index] != sorted_s[index]:
                return False

        return True
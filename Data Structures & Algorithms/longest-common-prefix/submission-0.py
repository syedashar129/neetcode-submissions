class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix):
                # chop off end of prefix
                prefix = prefix[:-1]

                # early return --> if empty return ""
                if not prefix:
                    return ""

        return prefix


# time: O(N * M)
# space: O(1)


# approach

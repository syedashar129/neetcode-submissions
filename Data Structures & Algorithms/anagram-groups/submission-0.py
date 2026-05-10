class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 2d array
        # define an anagram function
        # iterate and add into hashmap (keys = the letters - string, value = words)
        # return the values as lists inside a list

        anagram_map = {}
        for letter in strs:
            sorted_letter = "".join(sorted(letter))
            # not in map -- add
            if sorted_letter not in anagram_map:
                anagram_map[sorted_letter] = [letter]
            else:
                # in the map
                if sorted_letter in anagram_map:
                    anagram_map[sorted_letter].append(letter)

        # collect all the values
        return list(anagram_map.values())



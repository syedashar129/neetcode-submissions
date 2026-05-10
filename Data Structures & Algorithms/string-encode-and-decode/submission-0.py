class Solution:

    def encode(self, strs: List[str]) -> str:
        # create this into a single string (list str --> single str)
        # length# (ex: 4#)
        single_str_res = ""
        for string in strs:
            single_str_res += str(len(string)) + '#' + string
        return single_str_res #  4#neet4#code4#love4#you

    def decode(self, s: str) -> List[str]:
        # convert this into words from a unified string (single str --> list str)
        list_of_str = []
        i = 0

        while i < len(s):
            # parse out the length
            j = i

            while s[j] != '#':
                j += 1

            str_length = int(s[i:j])
            word = s[j+1 : j+1 + str_length]

            list_of_str.append(word)
            i = j+1 + str_length

        return list_of_str


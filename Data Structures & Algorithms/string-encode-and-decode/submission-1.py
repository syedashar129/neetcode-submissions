class Solution:

    def encode(self, strs: List[str]) -> str:
        # return encoded string
        res = ''
        for word in strs:
            word_len = len(word)
            res += str(word_len) + '#' + word
        return res


    def decode(self, s: str) -> List[str]:
        # return list of strings (4#neet4#code)
        # iterate
        # go till pound sign nad grab number
        # then parse from the str that amount
        # reset pointer to start of next string 
        res = []
        i = 0

        # for each word 
        while i < len(s):
            j = i
            
            # get number
            while s[j] != '#':
                j +=1

            word_length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + word_length])
            i = j + 1 + word_length
        return res
        



# approach
# add delimiter so we can decode it
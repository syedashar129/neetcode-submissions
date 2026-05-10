class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create pointers
        start_pointer = 0
        end_pointer = len(s) - 1

        # iterate 
        while start_pointer < end_pointer:
            while start_pointer < end_pointer and not s[start_pointer].isalnum():
                start_pointer += 1
            while end_pointer > start_pointer and not s[end_pointer].isalnum():
                end_pointer -= 1
            if s[start_pointer].lower() != s[end_pointer].lower():
                return False

            start_pointer += 1
            end_pointer -= 1
            
        return True

# notes
# do a check of .isalnum()
# 2 pointer - merging

# start pointer
# end pointer

# iterate on the string
# check if start pointer == end pointer
    # if yes 
        # increment start 
        # decremenet end
    # else
        # return False
# return True


# 2 things to think anout 
# 1. alphanumeric only
# 2. case insensitive


# time = N (iterate) --> O(n)
# space = 1 (pointer) --> O(1)

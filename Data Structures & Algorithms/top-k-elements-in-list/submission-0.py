class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmpa question
        # iterate through List
        # (key as number, value as how many)
        # return the k highest values from the map
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        sorted_nums = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        return sorted_nums[:k]
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if(len(nums)<k):
            return []

        freq_counter = {}

        k_elements = []

        for num in nums:
            if num in freq_counter:
                freq_counter[num] +=1
            else:
                freq_counter[num] = 1
        
        freq_set = set()
        for key in freq_counter:
            freq_set.add(freq_counter[key])
        freq_set = sorted(freq_set, reverse = True)

        i = 0
        while i != k:
            for key,value in freq_counter.items():
                if freq_counter[key] == freq_set[i]:
                    k_elements.append(key)

                if len(k_elements) == k:
                    return k_elements
            i+=1
        return k_elements





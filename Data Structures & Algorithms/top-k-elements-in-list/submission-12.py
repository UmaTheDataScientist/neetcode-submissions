class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq_list = []
        final_list = []
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]] = 1
        for key in seen:
            freq_list.append(seen[key])

        sorted_list_set = sorted(set(freq_list),reverse = True)

        for freq in sorted_list_set:
            for key in seen:
                if seen[key] == freq:
                    final_list.append(key)
                    if len(final_list) == k:
                        return final_list
        return final_list
                





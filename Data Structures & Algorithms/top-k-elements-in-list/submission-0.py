class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        dict_nums = {}
        for x in nums:
            if x not in dict_nums:
                dict_nums[x] = 1
            else:
                dict_nums[x]+=1
        sorted_keys_by_frq = sorted(dict_nums,key=dict_nums.get,reverse=True)
        return sorted_keys_by_frq[0:k]
        



            
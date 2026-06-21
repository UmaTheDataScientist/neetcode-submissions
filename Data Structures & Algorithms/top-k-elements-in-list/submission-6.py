class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]]+=1
            else:
                count_dict[nums[i]] = 1

        count_set = set()

        for key in count_dict:
            count_set.add(count_dict[key])

        count_set = sorted(count_set,reverse = True)

        output_list = []

        for freq in count_set:
            for key,value in count_dict.items():
                if freq == value:
                    output_list.append(key)
                
                if len(output_list) == k:
                    return output_list
        
        return output_list

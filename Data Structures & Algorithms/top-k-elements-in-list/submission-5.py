class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for ind_num in nums:
            if ind_num in count_dict:
                count_dict[ind_num]+=1
            else:
                count_dict[ind_num] = 1

        count_set = set()

        for key in count_dict:
            count_set.add(count_dict[key])
        
        count_set = sorted(count_set,reverse=True) #Count List

        output_list = []

        for freq in count_set:
            for key,value in count_dict.items():
                if value == freq:
                        output_list.append(key)
                if len(output_list) == k:
                    return output_list

        return output_list    
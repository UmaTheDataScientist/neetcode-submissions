class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_res = []
        dict_seen_num = {}
        for x in range(0,len(nums)):
            target_key = target - nums[x]
            if target_key in dict_seen_num:
                if x<dict_seen_num[target_key]:
                    list_res.append(x)
                    list_res.append(dict_seen_num[target_key])
                else:
                    list_res.append(dict_seen_num[target_key])
                    list_res.append(x)
                return list_res
            else:
                dict_seen_num[nums[x]]=x

            
        #     for y in range(x+1,len(nums)):
        #         if nums[x]+nums[y]== target:
        #             if x<y:
        #                 list_res.append(x)
        #                 list_res.append(y)
        #             else:
        #                 list_res.append(y)
        #                 list_res.append(x)
        return list_res



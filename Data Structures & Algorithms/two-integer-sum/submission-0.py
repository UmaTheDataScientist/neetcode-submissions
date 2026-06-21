class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_res = []
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]== target:
                    if x<y:
                        list_res.append(x)
                        list_res.append(y)
                    else:
                        list_res.append(y)
                        list_res.append(x)
        return list_res



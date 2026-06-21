class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(0,len(nums)):
            for point in range(x+1,len(nums)):
                if nums[x] == nums[point]:
                    return True
        return False


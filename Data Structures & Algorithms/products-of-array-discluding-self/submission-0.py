class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = [1]*len(nums)
        seen = {}
        for i in range(len(nums)):
            seen[i] = nums[i]
        for i in range(len(output_list)):
            for key in seen:
                if key!=i:
                    output_list[i] = output_list[i]*seen[key]
        return output_list




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        product_list = [1]*len(nums)

        #Left products
        for i in range(len(nums)):
            if i != 0:
                left_product*=nums[i-1]
                product_list[i] = left_product

        i = len(nums)-1
        right_product = 1

        while i>=0:
            if i!=len(nums)-1:
                right_product *= nums[i+1]
                product_list[i]*=right_product
            i = i -1

        return product_list


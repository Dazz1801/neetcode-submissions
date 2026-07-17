class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        sub_product_forward = [1]
        sub_product_backward = [1]

        prefix=1
        for i in range(1, len(nums)):
            sub_product_forward.append(prefix*nums[i-1])
            prefix*=nums[i-1]

        suffix=1
        for i in range(len(nums)-2,-1,-1):
            sub_product_backward.append(suffix*nums[i+1])
            suffix*=nums[i+1]
        result=[]
        for i in range(len(nums)):
            result.append(sub_product_forward[i]*sub_product_backward[len(nums)-i-1])
        return result
        
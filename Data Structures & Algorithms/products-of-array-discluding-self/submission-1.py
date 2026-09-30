class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        result = [1]* len(nums)
        
        for i in range(len(nums)):
            result[i] = 1*pre 
            pre=nums[i]*pre
        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post= post*nums[i]
  

        



        return result
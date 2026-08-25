class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)*2
        len1= len(nums)
        for i in range(len(nums)):
            ans[i]=ans[i+len1]=nums[i]
        return ans
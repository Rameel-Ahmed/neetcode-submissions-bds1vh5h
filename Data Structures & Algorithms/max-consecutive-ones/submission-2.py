class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones=0
        highestones=0
        for i in nums:
            if i==1:
                maxones+=1
                highestones=max(maxones, highestones)
            else:
                maxones=0
        return highestones

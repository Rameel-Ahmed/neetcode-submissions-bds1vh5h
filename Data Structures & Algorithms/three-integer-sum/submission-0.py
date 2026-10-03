class Solution:
    def two_sum_2(self, nums1:list[int], target: int):
        length = len(nums1)
        list2=[]
        l,r=0, length-1
        while(l<r):
            total = nums1[l]+nums1[r]
            if total==target:
                list2.append([-target,nums1[l],nums1[r]])
                left_value = nums1[l]
                right_value = nums1[r]
                while l < r and nums1[l] == left_value:
                    l += 1
                while l < r and nums1[r] == right_value:
                    r -= 1
            elif total>target:
                r-=1
            else:
                l+=1
        return list2

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list1=[]
        for i, a in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target_needed = -a
            abc = self.two_sum_2(nums[i+1:], target_needed)
            if abc:
                list1+=abc
        return list1
         
            




            
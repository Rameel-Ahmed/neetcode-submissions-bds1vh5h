class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        max_area_prev=0
        l,r=0,len(heights)-1
        while(l<r):
            min_height=min(heights[l],heights[r])
            length_diff=r-l
            max_area=min_height*length_diff
            if max_area>=max_area_prev:
                max_area_prev=max_area
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1

        return max_area_prev          

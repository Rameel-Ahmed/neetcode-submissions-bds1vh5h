# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        mid = n//2
        answer = guess(mid)
        if n<=1:
            return n
        while answer!= 0 and l<=r:
            if answer == -1:
                r=mid-1
                mid = (l+r)//2
                answer = guess(mid)
            else:
                l=mid+1
                mid = (l+r)//2
                answer = guess(mid)
        return mid

        
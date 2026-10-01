class Solution:
    def isPalindrome(self, s: str) -> bool:
        length=len(s)
        left = 0
        right = length-1
        while(left<right):
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower()==s[right].lower():
                        left+=1
                        right-=1
                    else:
                        return False
                else:
                    right-=1
            else:
                left +=1
        return True
            
                        


        
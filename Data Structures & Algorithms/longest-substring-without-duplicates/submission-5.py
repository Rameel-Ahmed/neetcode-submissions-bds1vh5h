class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list1 = []
        max_length = 0
        for char in s:
            if char not in list1:
                list1.append(char)
                length = len(list1)
                if length>max_length:
                    max_length = length
            else:
                list1=list1[list1.index(char)+1:]
                list1.append(char)
        return max_length


        
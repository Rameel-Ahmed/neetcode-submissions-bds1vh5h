class Solution:

    def encode(self, strs: List[str]) -> str:
        str2=""
        for str1 in strs:
            str2+=str1+":#:"
        print(str2)
        return str2

        

    def decode(self, s: str) -> List[str]:
        prev= 0
        result = []
        for i in range(len(s)):  
            if s[i:i+3] == ":#:":
                result.append(s[prev:i])
                prev = i+3

        return result



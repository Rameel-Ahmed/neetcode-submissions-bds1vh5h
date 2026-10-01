class Solution:

    def encode(self, strs: List[str]) -> str:
        str2=""
        for str1 in strs:
            str2+=str1+":#:"
        print(str2)
        return str2

        

    def decode(self, s: str) -> List[str]:
        result=s.split(":#:")
        result.pop()
        print(result)
        return result



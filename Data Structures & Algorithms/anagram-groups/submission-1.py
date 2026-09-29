class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            count = [0]*26
            
            for char in s:
                index = ord(char)-ord("a")
                count[index]+=1
            key = tuple(count)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        
        return list(seen.values())
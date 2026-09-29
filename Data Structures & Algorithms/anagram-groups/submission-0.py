class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            count = [0]*26
            
            for char in strs[i]:
                index = ord(char)-ord("a")
                count[index]+=1
            key = tuple(count)
            if key in seen:
                seen[key].append(strs[i])
            else:
                seen[key] = [strs[i]]
        
        return list(seen.values())
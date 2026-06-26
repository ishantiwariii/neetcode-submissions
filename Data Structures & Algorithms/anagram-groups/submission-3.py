class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmaps = {}
        for s in strs:
            count = [0]*26
            for ch in s : 
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            if key in hashmaps:
                hashmaps[key].append(s)
            else :
                hashmaps[key] = [s]
        
        return list(hashmaps.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for strng in strs:
            key = [0]*26
            for char in strng:
                key[ord(char)-ord('a')]+=1
            if tuple(key) in groups:
                groups[tuple(key)].append(strng)
            else:
                groups[tuple(key)] = [strng]
        result = []
        for val in groups.values():
            result.append(val)
        return result

            
        
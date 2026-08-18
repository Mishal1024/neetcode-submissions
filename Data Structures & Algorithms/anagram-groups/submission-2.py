class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            key = str(sorted(string))
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        return [group for group in hashmap.values()]
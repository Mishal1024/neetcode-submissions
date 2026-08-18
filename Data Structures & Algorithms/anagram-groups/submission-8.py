class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            temp = "".join(sorted(string))
            if temp not in groups.keys():
                groups[temp] = [string]
            else:
                groups[temp].append(string)
        return [item for item in groups.values()]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            if "".join(sorted(string)) not in groups.keys():
                groups["".join(sorted(string))] = [string]
            else:
                groups["".join(sorted(string))].append(string)
        return [item for item in groups.values()]
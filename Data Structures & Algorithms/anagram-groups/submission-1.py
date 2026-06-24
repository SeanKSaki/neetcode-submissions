class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert strings into sets compare sets if sets match then add to new list as a new list
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            groups.setdefault(key,[]).append(s)
        return list(groups.values())
        
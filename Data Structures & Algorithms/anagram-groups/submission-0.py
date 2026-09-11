class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newd={}
        for num in strs:
            keys=''.join(sorted(num))
            if keys in newd:
                newd[keys].append(num)
            else:
                newd[keys]=[num]
        return list(newd.values())
        
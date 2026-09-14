import itertools

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = itertools.permutations(nums)
        return [list(p) for p in perms]
        
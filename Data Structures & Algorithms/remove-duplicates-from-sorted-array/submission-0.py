class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newd = []
        for num in nums:
            if num not in newd:
                newd.append(num)
        
       
        nums[:] = newd
        
        
        return len(nums)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newl=[]
        for num in nums:
            if num not in newl:
                newl.append(num)

        for num in nums:
            if nums.count(num)>len(nums)//2:
               return num
                
                
                
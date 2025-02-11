class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in di:
                return [di[complement],i]
            di[nums[i]]=i
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for ind,val in enumerate(nums):
            complement=target-val
            if complement in di:
                return di[complement],ind
            di[val]=ind
        return []

        
        
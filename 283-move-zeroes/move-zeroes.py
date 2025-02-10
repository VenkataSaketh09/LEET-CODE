class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ptr]=nums[i]
                ptr+=1
        while ptr<len(nums):
            nums[ptr]=0
            ptr+=1

        
        
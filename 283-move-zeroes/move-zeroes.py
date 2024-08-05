class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indexes=0
        for i in range(len(nums)):
          if nums[i]!=0:
            nums[indexes]=nums[i]
            indexes+=1
        while indexes<len(nums):
          nums[indexes]=0
          indexes+=1


        
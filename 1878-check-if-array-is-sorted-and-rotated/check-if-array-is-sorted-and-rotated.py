class Solution:
    def check(self, nums: List[int]) -> bool:

        #slice technique
        i=1
        while i<len(nums):
            if nums[i-1]>nums[i]:
                break
            i+=1
        rotated_arr=nums[i:]+nums[:i]
        for i in range(1,len(nums)):
            if rotated_arr[i-1]>rotated_arr[i]:
                return False
        return True
        
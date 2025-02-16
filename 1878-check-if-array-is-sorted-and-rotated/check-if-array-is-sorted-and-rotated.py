class Solution:
    def check(self, nums: List[int]) -> bool:
        pointer=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                break
            pointer+=1
        nums=nums[pointer+1:]+nums[:pointer+1]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True
    


    
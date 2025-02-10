class Solution:
    def check(self, nums: List[int]) -> bool:
        ptr=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                break
            ptr+=1
        temp=nums[ptr+1:]+nums[:ptr+1]
        for i in range(len(nums)-1):
            if temp[i]>temp[i+1]:
                return False
        return True

        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #Boyeer-Moores Voting Algorithm
        #it has teo phases:1.candidate selection 2.verification

        #phase1 :
        count=0
        ele=None
        n=len(nums)
        for i in range(n):
            if count==0:
                count=1
                ele=nums[i]
            elif ele==nums[i]:
                count+=1
            else:
                count-=1
        #phase2:
        count=0
        for i in range(n):
            if nums[i]==ele:
                count+=1
        if count>n//2:
            return ele
        return -1
        

        
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        Sum=0
        l=r=0
        n=len(nums)
        ans=0
        while r<n:
            Sum+=nums[r]
            while nums[r]*(r-l+1)>Sum+k:
                Sum-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans

         
        
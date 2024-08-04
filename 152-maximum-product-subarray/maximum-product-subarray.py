class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      curMin,curMax=1,1
      ans=nums[0]
      for i in nums:
        values=(i,i*curMin,i*curMax)
        curMin,curMax=min(values),max(values)
        ans=max(ans,curMax)
      return ans

        
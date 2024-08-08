class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      #Two-Pointer Approach
      nums.sort()
      ans=[]
      for i in range(len(nums)):
        if i!=0 and nums[i]==nums[i-1]:
          continue
        
        j=i+1
        k=len(nums)-1
        while j<k:
          val=nums[i]+nums[j]+nums[k]
          if val>0:
            k-=1
          elif val<0:
            j+=1
          else:
            ans.append([nums[i], nums[j], nums[k]])  
            k-=1
            while j<k and nums[j]==nums[j-1]:
              j+=1
            while j<k and nums[k]==nums[k+1]:
              k-=1
      return ans
            


        
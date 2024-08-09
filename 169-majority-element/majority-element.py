class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      n=len(nums)//2
      di={}
      for i in nums:
        di[i]=di.get(i,0)+1
      for key,val in di.items():
        if val>n:
          return key
      
        
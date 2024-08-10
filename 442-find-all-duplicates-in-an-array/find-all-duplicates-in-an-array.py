class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      di={}
      for i in nums:
        di[i]=di.get(i,0)+1
      ans=[]
      for key,value in di.items():
        if value>1:
          ans.append(key)
      return ans
      
        
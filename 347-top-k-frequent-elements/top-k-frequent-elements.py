class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      di={}
      for i in nums:
        di[i]=di.get(i,0)+1
      ans=sorted(di.items(),key=lambda x:x[1],reverse=True)
      return [values for values,freq in ans[:k]]
        
        
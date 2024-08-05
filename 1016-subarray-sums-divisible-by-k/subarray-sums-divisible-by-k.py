class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
      prev_sum=0
      di={0:1}
      count=0
      for i in nums:
        prev_sum+=i
        rem=prev_sum%k
        if rem<0:
          rem+=k
        if rem in di:
          count+=di[rem]
          di[rem]+=1
        else:
          di[rem]=1
      return count
        
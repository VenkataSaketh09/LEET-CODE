class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      count=0
      cur_sum=0
      di={0:1}
      for i in nums:
        cur_sum+=i
        if cur_sum-k in di:
          count+=di[cur_sum-k]
        di[cur_sum]=di.get(cur_sum,0)+1
      return count
        
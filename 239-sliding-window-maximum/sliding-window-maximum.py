from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      res=[]
      n=len(nums)
      #Brute Force 

      # for i in range(n-k+1):
      #   max_ele=nums[i]
      #   for j in range(i,i+k):
      #     max_ele=max(max_ele,nums[j])
      #   res.append(max_ele)
      # return res

      dque=deque()
      for i in range(n):
        if dque and dque[0]<i-k+1:
          dque.popleft()
        while dque and nums[dque[-1]]<nums[i]:
          dque.pop()
        dque.append(i)
        if i>=k-1:
          res.append(nums[dque[0]])
      return res
        
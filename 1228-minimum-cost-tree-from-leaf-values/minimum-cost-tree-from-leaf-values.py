class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
      ans=0
      stack=[float('inf')]
      for i in arr:
        while stack and stack[-1]<=i:
          val=stack.pop()
          ans+=val*min(stack[-1],i)
        stack.append(i)
      while len(stack)>2:
        ans+=stack.pop()*stack[-1]
      return ans
        
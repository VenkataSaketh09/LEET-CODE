class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
      n=len(arr)
      nse=[n]*n
      pse=[-1]*n
      stack=[]
      for i in range(n-1,-1,-1):
        while stack and arr[i]<=arr[stack[-1]]:
          stack.pop()
        if stack:
          nse[i]=stack[-1]
        stack.append(i)
      stack=[]
      for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
          stack.pop()
        if stack:
          pse[i]=stack[-1]
        stack.append(i)
      total=0
      modulo=10**9+7
      for i in range(len(arr)):
        left=i-pse[i]
        right=nse[i]-i
        total=(total+(left*right*arr[i])%modulo)%modulo
      return total
      
      
    
         



        
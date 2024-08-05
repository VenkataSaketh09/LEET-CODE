class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      def dfs(left,right,string):
        if len(string)==n*2:
          ans.append(string)
          return
        if left<n:
          dfs(left+1,right,string+'(')
        if right<left:
          dfs(left,right+1,string+')')
      ans=[]
      dfs(0,0,'')
      return ans
      
        
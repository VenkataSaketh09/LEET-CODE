class Solution:
    def numTrees(self, n: int) -> int:
      dp=[0]*(n+1)
      dp[0]=1  #1 empty tree
      dp[1]=1  #1 tree with 1 node
      for i in range(2,n+1):
        for j in range(1,i+1):
          dp[i]+=dp[j-1]*dp[i-j]
      return dp[n]

      #dp[j-1] represents number of BST's for left sub tree.
      #dp[i-j] the remaining the elemrnst greater than j represents number of BST's for right subtree.

        
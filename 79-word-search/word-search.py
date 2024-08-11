class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      for i in range(len(board)):
        for j in range(len(board[0])):
          if board[i][j]==word[0] and self.searching(board,i,j,0,word):
            return True
      return False
    def searching(self,board,i,j,index,word):
      if index==len(word):
        return True
      if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[index]:
        return False
      #to avoid reuse
      temp=board[i][j]
      board[i][j]='#'
      flag=self.searching(board,i+1,j,index+1,word) or self.searching(board,i-1,j,index+1,word) or self.searching(board,i,j+1,index+1,word) or self.searching(board,i,j-1,index+1,word)
      board[i][j]=temp
      return flag


        
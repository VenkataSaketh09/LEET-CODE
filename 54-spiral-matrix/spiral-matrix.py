class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      m=len(matrix)  #rows
      n=len(matrix[0])  #columns
      left,top=0,0
      right=n-1
      bottom=m-1

      ans=[]

      while (top<=bottom and left<=right):
        for i in range(left,right+1):
          ans.append(matrix[top][i])
        top+=1

        for i in range(top,bottom+1):
          ans.append(matrix[i][right])
        right-=1
        
        if(top<=bottom):
          for i in range(right,left-1,-1):
            ans.append(matrix[bottom][i])
          bottom-=1
        
        if(left<=right):
          for i in range(bottom,top-1,-1):
            ans.append(matrix[i][left])
          left+=1
      return ans
          




      
        
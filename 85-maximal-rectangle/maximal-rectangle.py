class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
      if not matrix:
        return 0
      rows=len(matrix)
      cols=len(matrix[0])
      max_area=0
      histogram_heights=[0]*(cols+1)
      for row in matrix:
        for j in range(cols):
          histogram_heights[j]=histogram_heights[j]+1 if row[j]=='1' else 0
      
        stack = []
        for i in range(len(histogram_heights)):
          while stack and histogram_heights[i] < histogram_heights[stack[-1]]:
            h = histogram_heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
          stack.append(i)

      return max_area
      


        
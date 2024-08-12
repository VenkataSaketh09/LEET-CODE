class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      stack=[]
      max_area=0
      for ind,height in enumerate(heights):
        start=ind
        while stack and height<stack[-1][1]:
          index,hght=stack.pop()
          max_area=max(max_area,hght*(ind-index))
          start=index
        stack.append((start,height))
      for indexes,hghts in stack:
        max_area=max(max_area,hghts*(len(heights)-indexes))
      return max_area
        
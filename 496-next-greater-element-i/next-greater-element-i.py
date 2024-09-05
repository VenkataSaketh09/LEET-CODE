class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ans=[]
      di={}
      for i in reversed(nums2):
        while ans and ans[-1]<=i:
          ans.pop()
        di[i]=ans[-1] if ans else -1
        ans.append(i)
      return [di[num] for num in nums1]


        
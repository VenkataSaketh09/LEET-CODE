class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di={}
        stack=[]
        for i in reversed(nums2):
            while stack and stack[-1]<=i:
                stack.pop()
            di[i]=stack[-1] if stack else -1
            stack.append(i)
        return [di[num] for num in nums1]

            
        
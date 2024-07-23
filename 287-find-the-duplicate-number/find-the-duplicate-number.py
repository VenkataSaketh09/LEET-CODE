class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            di[i]=di.get(i,0)+1
        for i in di:
            if di[i]>1:
                return i
        
        
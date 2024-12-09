class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di={}
        ans=0
        more_repeat=0
        for i in nums:
            di[i]=di.get(i,0)+1
            if di[i]>more_repeat:
                ans=i
                more_repeat=di[i]
        return ans
        
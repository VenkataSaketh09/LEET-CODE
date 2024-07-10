class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        while nums:
            p1,p2=nums.pop(),nums.pop()
            ans+=p2
        return ans

        
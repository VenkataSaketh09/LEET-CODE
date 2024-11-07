class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # di={}
        # for i in nums:
        #     di[i]=di.get(i,0)+1
        # for i in di:
        #     if di[i]==1:
        #         return i
        
        #using the xor is optimal approach
        xorr=0
        for i in nums:
            xorr^=i

        return xorr

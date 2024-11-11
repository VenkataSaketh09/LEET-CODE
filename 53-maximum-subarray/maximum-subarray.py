class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value=float('-inf')
        Sum=0
        for i in nums:
            Sum+=i
            if Sum>max_value:
                max_value=Sum
            if Sum<0:
                Sum=0
        return max_value 
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_arr=0
        actual_sum_arr=0
        for i in range(len(nums)):
            sum_arr+=nums[i]
            actual_sum_arr+=i+1
        return actual_sum_arr-sum_arr
        
        
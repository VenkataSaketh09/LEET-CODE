class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di={0:1}
        count=0
        Sum=0
        for i in range(len(nums)):
            Sum+=nums[i]
            if Sum-k in di:
                count+=di[Sum-k]
            if Sum in di:
                di[Sum]+=1
            if Sum not in di:
                di[Sum]=1
        return count
            
        
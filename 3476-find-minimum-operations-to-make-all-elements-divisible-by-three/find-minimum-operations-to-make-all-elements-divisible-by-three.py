class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            rem=i%3
            if rem==1 or rem==2:
                count+=1
        return count


        
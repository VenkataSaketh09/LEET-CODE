class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ind1,ind2=-1,-1
        for i in range(len(nums)):
            if nums[i]==target:
                if ind1==-1:
                    ind1=i
                ind2=i
        return [ind1,ind2]
        
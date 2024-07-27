class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right=0
        for ind in range(len(nums)):
            if ind>right:
                return False
            if nums[ind]+ind>right:
                right=nums[ind]+ind
        return True
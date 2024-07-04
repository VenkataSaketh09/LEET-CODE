class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
        data=set()
        for i in nums:
            if i in data:
                return True
            data.add(i)
        return False

        
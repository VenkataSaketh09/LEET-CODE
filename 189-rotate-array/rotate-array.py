class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        rotation_point=len(nums)-k
        new_arr=nums[0:rotation_point]
        nums[0:rotation_point]=[]
        nums.extend(new_arr)

        
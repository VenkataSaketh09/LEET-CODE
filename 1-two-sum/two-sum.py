class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for index,item in enumerate(nums):
            complement_value=target-item
            if complement_value in hash_map:
                return hash_map[complement_value],index
            hash_map[item]=index
        return []

        
        
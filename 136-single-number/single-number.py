class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #xor operation
        xor=0
        for i in nums:
            xor^=i
        return xor
        
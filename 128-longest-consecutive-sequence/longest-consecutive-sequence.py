class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        maxi=float('-inf')
        count=0
        longest=1
        for i in nums:
            if i-1==maxi:
                count+=1
                maxi=i
            elif i!=maxi:
                count=1
                maxi=i
            longest=max(longest,count)
        return longest
        
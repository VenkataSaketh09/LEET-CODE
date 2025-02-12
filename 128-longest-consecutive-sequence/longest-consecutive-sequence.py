class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        count=0
        nums.sort()
        longest=1
        maxi=float('-inf')
        for i in nums:
            if i-1==maxi:
                count+=1
                maxi=i
            elif i!=maxi:  #first iteration
                count=1
                maxi=i
            longest=max(longest,count)
        return longest
            

        
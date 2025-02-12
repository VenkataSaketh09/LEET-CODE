class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        # count=0
        # nums.sort()
        # longest=1
        # maxi=float('-inf')
        # for i in nums:
        #     if i-1==maxi:
        #         count+=1
        #         maxi=i
        #     elif i!=maxi:  #first iteration
        #         count=1
        #         maxi=i
        #     longest=max(longest,count)
        # return longest


        #optimal Approach
        data=set(nums)
        count=0
        longest=1
        for i in data:
            if i-1 not  in data:
                count=1
                temp=i
                while temp+1 in data:
                    count+=1
                    temp+=1
            longest=max(longest,count)
        return longest


            

        
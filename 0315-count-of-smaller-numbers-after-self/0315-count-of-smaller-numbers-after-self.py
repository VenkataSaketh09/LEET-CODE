import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list=[]
        ans=[]
        for i in nums[::-1]:
            val=bisect.bisect_left(sorted_list,i)
            ans.append(val)
            bisect.insort_left(sorted_list,i)
        return ans[::-1]
        
        
import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals=sorted([[beg,end,indx] for indx,[beg,end] in enumerate(intervals)])
        ans=[-1]*len(intervals)
        begin_values=[beg for beg,end,indx in intervals]
        for beg,end,indx in intervals:
            val=bisect.bisect_left(begin_values,end)
            if val!=len(begin_values):
                ans[indx]=intervals[val][-1]
        return ans


        
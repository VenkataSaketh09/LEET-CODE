class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        di={}
        res=[]
        for i in nums:
            di[i]=di.get(i,0)+1
        for item,val in di.items():
            if val>len(nums)//3:
                res.append(item)
        return res


        
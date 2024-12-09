class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        res=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        ptr1=ptr2=0
        while ptr1<len(pos) and ptr2<len(neg):
            res.append(pos[ptr1])
            res.append(neg[ptr2])
            ptr1+=1
            ptr2+=1
        while ptr1<len(pos):
            res.append(pos[ptr1])
            ptr1+=1
        while ptr2<len(neg):
            res.append(neg[ptr2])
            ptr2+=1
        return res
        
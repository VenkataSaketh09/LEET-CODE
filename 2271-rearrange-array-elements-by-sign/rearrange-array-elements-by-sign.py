class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_arr=[]
        neg_arr=[]
        for i in nums:
            if i>=0:
                pos_arr.append(i)
            else:
                neg_arr.append(i)
        modified_arr=[]
        for i,j in zip(pos_arr,neg_arr):
            modified_arr.append(i)
            modified_arr.append(j)
        return modified_arr    
        
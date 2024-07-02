class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=sorted(nums1)
        b=sorted(nums2)
        i=j=0
        ans=[]
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                i+=1
            elif b[j]<a[i]:
                j+=1
            else:
                ans.append(a[i])
                i+=1
                j+=1
        return ans


        
        
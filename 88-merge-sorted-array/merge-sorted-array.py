class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        array1_ind=len(nums1)-1
        while m>0 and n>0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[array1_ind]=nums2[n-1]
                n-=1
            else:
                nums1[array1_ind]=nums1[m-1]
                m-=1
            array1_ind-=1
        while n>0:
            nums1[array1_ind]=nums2[n-1]
            n-=1
            array1_ind-=1


        
        
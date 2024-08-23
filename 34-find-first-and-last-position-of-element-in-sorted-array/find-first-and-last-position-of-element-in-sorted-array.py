class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # ind1,ind2=-1,-1
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         if ind1==-1:
        #             ind1=i
        #         ind2=i
        # return [ind1,ind2]
        def finding_first(arr,target):
          low=0
          high=len(arr)-1
          first=-1
          while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
              first=mid
              high=mid-1
            elif arr[mid]<target:
              low=mid+1
            else:
              high=mid-1
          return first
        def finding_last(arr,target):
          low=0
          high=len(arr)-1
          last=-1
          while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
              last=mid
              low=mid+1
            elif arr[mid]<target:
              low=mid+1
            else:
              high=mid-1
          return last
        def returning(arr,target):
          first=finding_first(arr,target)
          last=finding_last(arr,target)
          if first==-1:
            return [-1,-1]
          return [first,last]
        ans=returning(nums,target)
        return ans

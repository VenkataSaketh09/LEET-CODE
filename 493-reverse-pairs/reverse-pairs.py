class Solution:
    def reversePairs(self, nums: List[int]) -> int:
      self.count=0
      def merging(left_arr,right_arr):
        i,j=0,0
        while i<len(left_arr) and j<len(right_arr):
          if left_arr[i]>2*right_arr[j]:
            self.count+=len(left_arr)-i
            j+=1
          else:
            i+=1
        low,high=0,0
        ans=[]
        while low<len(left_arr) and high<len(right_arr):
          if left_arr[low]<right_arr[high]:
            ans.append(left_arr[low])
            low+=1
          else:
            ans.append(right_arr[high])
            high+=1
        return ans+left_arr[low:]+right_arr[high:]
      def merge_sort(arr):
        if len(arr)<=1:
          return arr
        mid=(len(arr)//2)
        left_arr=merge_sort(arr[:mid])
        right_arr=merge_sort(arr[mid:])
        return merging(left_arr,right_arr)
      nums=merge_sort(nums)
      return self.count
      
        
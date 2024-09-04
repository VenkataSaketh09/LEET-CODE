# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
      def flatten(nested_list):
        ans=[]
        for val in nested_list:
          if val.isInteger():
            ans.append(val.getInteger())
          else:
            ans.extend(flatten(val.getList()))
        return ans

      self.flattened=flatten(nestedList)
      self.ind=0
    
    def next(self) -> int:
      self.ind+=1
      return self.flattened[self.ind-1]

    def hasNext(self) -> bool:
      return self.ind<len(self.flattened)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
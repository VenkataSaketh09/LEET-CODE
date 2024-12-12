class Solution:
    def generateRow(self,row):
        temp=1
        result=[1]
        for i in range(1,row):
            temp=temp*(row-i)
            temp=temp//i
            result.append(temp)
        return result
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            data=self.generateRow(i)
            ans.append(data)
        return ans
        
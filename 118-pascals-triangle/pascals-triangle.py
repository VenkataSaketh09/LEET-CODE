class Solution:
    def generateRow(self,r):
        temp=[1]
        val=1
        for i in range(1,r):
            val=(val*(r-i))//i
            temp.append(val)
        return temp
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            data=self.generateRow(i+1)
            ans.append(data)
        return ans


        
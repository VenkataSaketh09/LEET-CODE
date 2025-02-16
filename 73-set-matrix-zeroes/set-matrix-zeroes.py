class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr1=[]#row number
        arr2=[]#col number
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    arr1.append(i)
                    arr2.append(j)
        for i in arr1:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in arr2:
            for j in range(len(matrix)):
                matrix[j][i]=0


        
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        ans=str(int(s)+1)
        val=[int(x)for x in ans]
        return val

        
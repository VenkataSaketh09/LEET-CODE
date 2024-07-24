class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=''
        n1=len(a)-1
        n2=len(b)-1
        carry=0
        while n1>=0 or n2>=0 or carry!=0:
            if n1>=0:
                carry+=int(a[n1])
                n1-=1
            if n2>=0:
                carry+=int(b[n2])
                n2-=1
            res+=str(carry%2)
            carry//=2
        return res[::-1]


        
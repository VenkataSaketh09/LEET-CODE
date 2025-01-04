class Solution:
    def frequencySort(self, s: str) -> str:
        di={}
        ans=''
        for i in s:
            di[i]=di.get(i,0)+1
        keys_list=sorted(di.items(),key=lambda x:x[1],reverse=True)
        for i,j in keys_list:
            ans+=i*j
        return ans

        
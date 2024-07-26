class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        for word in strs:
            val=''.join(sorted(word))
            if val not in di:
                di[val]=[word]
            else:
                di[val].append(word)
        return list(di.values())
        
        
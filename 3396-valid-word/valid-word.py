class Solution:
    def isValid(self, word: str) -> bool:
        c1=0
        c2=0
        val='aeiouAEIOU'
        if len(word)<=2:
            return False
        for i in range(len(word)):
            if word[i].isalpha():
                if word[i] in val:
                    c1+=1
                else:
                    c2+=1
            else:
                if word[i]=='@' or word[i]=='#' or word[i]=='$':
                    return False
        if c1>=1 and c2>=1:
            return True
        else:
            return False


        
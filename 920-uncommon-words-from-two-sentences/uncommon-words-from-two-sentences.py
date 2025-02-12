class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        dic={}
        bab=[]
        for i in s1:
            dic[i]=1+dic.get(i,0)
        for j in s2:
            dic[j]=1+dic.get(j,0)
        
        for a,b in dic.items():
            if b==1:
                bab.append(a)
        return bab

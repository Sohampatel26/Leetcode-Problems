class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0]=="0":
            return 0
        ways=[0]*(len(s)+1)
        ways[0],ways[1]=1,1

        for i in range(2,len(s)+1):
            if 0<int(s[i-1])<=9:
                ways[i]=ways[i-1]
            if 10<=int(s[i-2:i])<27:
                ways[i]+=ways[i-2]
        
        return ways[-1]
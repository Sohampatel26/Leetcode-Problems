class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispal(s):
            return s==s[::-1]
        a=[]
        maxi=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                if ispal(s[i:j+1]):
                    count=len(s[i:j+1])
                    if count>maxi:
                        a.append(s[i:j+1])
                    maxi=max(maxi,count)
                    
        return a[-1]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        l=0
        leng=0
        maxl=0
        for r in range(len(s)):
            while s[r] in stack:
                stack.remove(s[l])
                leng-=1
                l+=1
            stack.append(s[r])
            leng+=1
            maxl=max(leng,maxl)
        return maxl

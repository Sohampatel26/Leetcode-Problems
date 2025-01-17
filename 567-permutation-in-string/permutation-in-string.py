class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        cs1=[0]*26
        cs2=[0]*26
        for i in range(len(s1)):
            cs1[ord(s1[i])-ord('a')]+=1
            cs2[ord(s2[i])-ord('a')]+=1
        count=0
        for i in range(26):
            if cs1[i]==cs2[i]:
                count+=1
        
        l=0
        for r in range(len(s1),len(s2)):
            if count==26:
                return True

            ind=ord(s2[r])-ord('a')
            cs2[ind]+=1
            if cs2[ind]==cs1[ind]:
                count+=1
            elif cs2[ind]-1==cs1[ind]:
                count-=1

            ind=ord(s2[l])-ord('a')
            cs2[ind]-=1
            if cs2[ind]==cs1[ind]:
                count+=1
            elif cs2[ind]+1==cs1[ind]:
                count-=1
            l+=1
        return count == 26
            
            
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        add=0
        n=len(digits)
        for i in range(n-1,-1,-1):
            add+=(10**(n-i-1))*digits[i]
        add=add+1

        while add!=0:
            a=add%10
            add=add//10
            res.append(a)
        return res[::-1]





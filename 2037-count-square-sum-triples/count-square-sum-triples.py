class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            isquare=i*i
            for j in range(1,n+1):
                sumsq=isquare+(j*j)
                roots=int(math.sqrt(sumsq))
                if roots<=n and roots**2==sumsq:
                    count+=1
        return count
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        s=[[] for _ in range(len(nums)+1)]
        res=[]

        for n,v in count.items():
            s[v].append(n)

        for a in range(len(nums),-1,-1):
            for c in s[a]:
                res.append(c)
                k-=1
                if k==0:
                    return res


        
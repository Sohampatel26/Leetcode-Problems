class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        for i in range(k):
            mini=max(count.values())
            for i in count:
                if count[i]==mini:
                    res.append(i)
                    del count[i]
                    break
        
        return res


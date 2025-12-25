class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic=defaultdict(list)
        for i,v in enumerate(nums):
            if v in dic:
                for val in dic[v]:
                    if abs(val-i)<=k:
                        return True
            dic[v].append(i)
        
        return False
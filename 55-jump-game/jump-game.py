from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i>=len(nums)-1:
                return True
            if nums[i]>0:
                for a in range(1,nums[i]+1):
                    if dfs(i+a):
                        return True
            
            return False
        return dfs(0)
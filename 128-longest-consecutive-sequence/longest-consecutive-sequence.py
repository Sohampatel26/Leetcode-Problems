class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if nums==[0]:
            return 1
        maxi=0
        se=set(nums)
        for i in se:
            if i-1 not in se:
                res=1
                while i+1 in se:
                    res+=1
                    i+=1
                maxi=max(maxi,res)
        return maxi
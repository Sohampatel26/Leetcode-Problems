class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum=0
        maxi=nums[0]
        for i in range(len(nums)):
            if csum<0:
                csum=0
            csum+=nums[i]
            maxi=max(csum,maxi)

        return maxi 
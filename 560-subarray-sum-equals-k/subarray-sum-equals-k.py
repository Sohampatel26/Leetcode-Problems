class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        runningtotal=0
        count=0

        for i in nums:
            runningtotal+=i
            if runningtotal-k in seen:
                count+=seen[runningtotal-k]

            seen[runningtotal]=1+seen.get(runningtotal,0)
        
        return count

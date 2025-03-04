class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        se=set()
        se.add(0)
        target=sum(nums)/2

        if sum(nums)%2!=0:
            return False

        for i in nums:
            set2=set()
            for a in se:
                if i+a==target:
                    return True
                set2.add(i+a)
            se.update(set2)
        return False

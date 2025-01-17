class Solution(object):
    def twoSum(self, nums, target):
        pmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in pmap:
                return [pmap[diff],i]
            pmap[n]=i
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=len(nums)-1
        l=0
        while l<=r:
            if target==nums[(l+r)//2]:
                return (l+r)//2
            if target>nums[(l+r)//2]:
                l=((l+r)//2)+1
            if target<nums[(l+r)//2]:
                r=((l+r)//2)-1
            
        return -1
class Solution(object):
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while  l<=r:
            if target==nums[(r+l)//2]:
                return (r+l)//2
            elif target>nums[(r+l)//2]:
                l=((r+l)//2)+1
            elif target<nums[(r+l)//2]:
                r=((r+l)//2)-1
        return -1
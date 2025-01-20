class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                
                l = m + 1
            else:
                
                r = m
        mini=l

        if target<nums[len(nums)-1]:
            le=mini
            ri=len(nums)-1
            while le<=ri:
                mi=(le+ri)//2
                if nums[mi]>target:
                    ri-=1
                elif nums[mi]<target:
                    le+=1
                else:
                    return mi
        
        elif target>nums[len(nums)-1]:
            le=0
            ri=mini-1
            while le<=ri:
                mi=(le+ri)//2
                if nums[mi]>target:
                    ri-=1
                elif nums[mi]<target:
                    le+=1
                else:
                    return mi
        elif target==nums[len(nums)-1]:
            return len(nums)-1

        return -1
                


        
        
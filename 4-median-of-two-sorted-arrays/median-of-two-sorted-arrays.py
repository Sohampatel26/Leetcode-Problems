class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        n=sorted(n)

        l=len(n)

        if l%2==0:
            return (n[l//2]+n[(l//2)-1])/2
        return n[(l//2)]
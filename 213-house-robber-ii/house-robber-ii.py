class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        def hr(babu):
            if not babu:
                return 0
            if len(babu)==1:
                return babu[0]
            arr=[0]*len(babu)
            arr[0]=babu[0]
            arr[1]=max(babu[0],babu[1])
            maxi=0
            
            for i in range(2,len(babu)):
                arr[i]= max(babu[i]+arr[i-2],arr[i-1])
            
            return arr[-1]

        return max(hr(nums[1:]),hr(nums[:-1]))
                
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty array
        
        max_product = min_product = result = nums[0]  # ✅ Initialize
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num < 0:  # Swap min and max when num is negative
                max_product, min_product = min_product, max_product
            
            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)

            result = max(result, max_product)  # ✅ Track global max
        
        return result  # ✅ Return the maximum product found

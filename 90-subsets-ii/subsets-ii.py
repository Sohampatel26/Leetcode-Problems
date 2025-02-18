# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res=[]
#         nums.sort()
#         def rec(start,path):
#             res.append(path[:])

#             for i in range(start,len(nums)):
#                 path.append(nums[i])
#                 rec(i+1,path)
#                 path.pop()

#         rec(0,[])

        
#         res = set(tuple(subset) for subset in res)  
#         return [list(subset) for subset in res]  
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # ✅ Step 1: Sort to group duplicates together

        def backtrack(start, path):
            res.append(path[:])  # ✅ Step 2: Add the current subset

            for i in range(start, len(nums)):
                # ✅ Step 3: Skip duplicate elements at the same recursion level
                if i > start and nums[i] == nums[i - 1]:  
                    continue  

                path.append(nums[i])  # ✅ Step 4: Pick the number
                backtrack(i + 1, path)  # ✅ Step 5: Recur with the next index
                path.pop()  # ✅ Step 6: Undo the choice (Backtrack)

        backtrack(0, [])
        return res

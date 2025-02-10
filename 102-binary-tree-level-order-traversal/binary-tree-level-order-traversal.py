# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue=deque([root])
        res=[]

        while queue:
            size=len(queue)
            level=[]

            for _ in range(size):
                a=queue.popleft()
                level.append(a.val)

                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                
            res.append(level)
            
        return res
            
            

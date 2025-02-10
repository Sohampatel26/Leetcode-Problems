# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result=[]
        queue=deque([root])

        while queue:
            l=len(queue)
            for i in range(l):
                a=queue.popleft()
                if i==l-1:
                    result.append(a.val)
                if a.left:
                        queue.append(a.left)
                if a.right:
                        queue.append(a.right)
        
        return result
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue=deque([root])
        lis=[]
    
        while queue:
            lis=[]
            l=len(queue)
            for i in range(l):
                a=queue.popleft()
                if a:
                    lis.append(a.val)
                    queue.append(a.left)
                    queue.append(a.right)
                else:
                    lis.append(None)
            if lis != lis[::-1]:
                return False
            
        return True
                



        
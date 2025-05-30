# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # queue=deque([root])
        # lis=[]
    
        # while queue:
        #     lis=[]
        #     l=len(queue)
        #     for i in range(l):
        #         a=queue.popleft()
        #         if a:
        #             lis.append(a.val)
        #             queue.append(a.left)
        #             queue.append(a.right)
        #         else:
        #             lis.append(None)
        #     if lis != lis[::-1]:
        #         return False
            
        # return True
            
        if not root:
            return True
        
        def dfs(p,q):
            if not p and not q:
                return True
            if p and not q or q and not p:
                return False
            
            if p.val!=q.val:
                return False

            return dfs(p.left,q.right) and dfs(q.left ,p.right)
        
        return dfs(root.left,root.right)




        
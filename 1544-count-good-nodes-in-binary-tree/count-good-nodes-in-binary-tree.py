# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxsofar):
            if not root:
                return 0
            
            if root.val>=maxsofar:
                gg=1
            else:
                gg=0
            maxsofar=max(maxsofar,root.val)
            
            return gg+dfs(root.left,maxsofar)+dfs(root.right,maxsofar)
        
        return dfs(root,root.val)
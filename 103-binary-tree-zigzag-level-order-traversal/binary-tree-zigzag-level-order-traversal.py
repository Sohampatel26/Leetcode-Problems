# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue=deque([root])
        result=[]
        f=0
        while queue:
            f+=1
            lis=[]
            l=len(queue)
            for i in range(l):
                a=queue.popleft()
                lis.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            
            if f%2==1:
                result.append(lis)
            
            else:
                result.append(lis[::-1])
        return result
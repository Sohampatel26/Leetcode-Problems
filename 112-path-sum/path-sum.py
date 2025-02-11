class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1️⃣ Assume we are at the deepest level (Base Case)
        if not root:
            return False  # If there's no node, no path exists

        # If this is a leaf node, check if the remaining sum is exactly this node's value
        
        if targetSum == root.val and not root.left and not root.right:
            return True  # ✅ If true, we've found a valid path

        # 2️⃣ Serve my part at this node
        # Subtract the current node value from targetSum

        remaining_sum = targetSum - root.val

        # 3️⃣ Ask my children to do the same (Recursive Calls)
        # Recurse on left and right children
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum)

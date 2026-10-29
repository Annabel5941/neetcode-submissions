# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def visitChild(self, node, depth):
        leftDepth, rightDepth = depth, depth
        #try left
        if node.left is not None:
            leftDepth = self.visitChild(node.left, depth+1)

        #try right
        if node.right is not None:
            rightDepth = self.visitChild(node.right, depth+1)

        return max(leftDepth, rightDepth)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            return self.visitChild(root, 1)
        
        return 0
        
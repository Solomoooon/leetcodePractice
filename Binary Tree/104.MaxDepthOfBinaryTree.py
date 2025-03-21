# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    def traverse(cur):
        if cur is None:
            return 0
        if cur.left is None and cur.right is None:
            return 1
        return 1 + max(traverse(cur.left), traverse(cur.right))

    return traverse(root)

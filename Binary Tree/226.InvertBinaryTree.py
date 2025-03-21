# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    cur = root

    def invert(cur):
        if cur is None:
            return
        if cur.left is None and cur.right is None:
            return
        tmp = cur.left
        cur.left = cur.right
        cur.right = tmp
        invert(cur.left)
        invert(cur.right)

    invert(cur)
    return cur

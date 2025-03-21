# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    def traverse(cur):
        if not cur:
            return False
        left = traverse(cur.left)
        right = traverse(cur.right)

        mid = cur == p or cur == q

        if mid + left + right >= 2:
            self.ans = cur

        return mid or left or right

    traverse(root)
    return self.ans

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.diameter = 0

    def traverse(cur):
        if cur is None:
            return 0
        left = traverse(cur.left)
        right = traverse(cur.right)

        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

    traverse(root)
    return self.diameter

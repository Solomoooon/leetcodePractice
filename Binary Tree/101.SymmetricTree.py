class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def valid(n1, n2):
        if n1 is None and n2 is None:
            return True

        if n1 is None or n2 is None:
            return False

        return (
            n1.val == n2.val and valid(n1.left, n2.right) and valid(n1.right, n2.left)
        )
        # 镜像说明只要两个靠外侧或者两个靠里侧的node相同就行

    return valid(root, root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    def traverse(cur, num):
        if num == k:
            return cur.val
        if cur.left == None and cur.right == None:
            num += 1
            return
        if cur.left:
            traverse(cur.left, num)
            num += 1
        if cur.right:
            traverse(cur.right, num)
            num += 1

    return traverse(root, 0)

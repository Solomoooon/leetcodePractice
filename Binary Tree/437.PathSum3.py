class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    ans = 0

    def traverse(cur, sum):
        if cur is None:
            return
        if sum + cur.val == targetSum:
            nonlocal ans
            ans += 1
        if cur.left is None and cur.right is None:
            return

        if cur.left:
            sum = sum + cur.val
            traverse(cur.left, sum)
            sum = sum - cur.val

        if cur.right:
            sum = sum + cur.val
            traverse(cur.right, sum)
            sum = sum - cur.val
        return

    traverse(root, 0)
    return ans

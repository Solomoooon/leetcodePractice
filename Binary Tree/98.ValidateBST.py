class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def search(cur, minval=-math.inf, maxval=math.inf):
        if not cur:
            return True

        if cur.val <= minval or cur.val >= maxval:
            return False

        # 判断条件

        return search(cur.right, cur.val, maxval) and search(cur.left, minval, cur.val)
        # 当向右traverse的时候，minval更新因为接下来的一定要比这个大

    return search(root)

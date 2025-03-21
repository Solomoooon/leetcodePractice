class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(self, root: Optional[TreeNode]) -> None:
    def flattenTree(cur):
        if cur is None:
            return None
        if cur.left is None and cur.right is None:
            return cur
        lefttail = flattenTree(cur.left)
        righttail = flattenTree(cur.right)
        if lefttail:
            lefttail.right = cur.right
            # 让左尾部的右边指向cur.right
            cur.right = cur.left
            # cur.right指向cur.left,合并两边链表
            cur.left = None
            # 删除左链表

        return righttail if righttail else lefttail
        # 如果左右边都有，那说明左右合并了，返回右边。如果只有右边。返回右边。否者就只剩左边了，返回左边

    flattenTree(root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    levels = []

    def traverse(cur, level):
        if len(levels) == level:
            # 正常len(levels) = level + 1，如果是这种情况说明level刚刚+1了，cur到新一层了。所以要levels创一个新的subarray
            levels.append([])

        levels[level].append(cur)
        # 把当前node cur加到对应的levels[level]里

        if cur.left:
            traverse(cur.left, level + 1)
        if cur.right:
            traverse(cur.right, level + 1)

    traverse(root, 0)
    return levels

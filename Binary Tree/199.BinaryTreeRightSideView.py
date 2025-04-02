from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    nextlevel = deque([root])
    # 初始状态是把root放进nextlevel里
    rightside = []
    # 解题思路是用两个queue做BFS。
    while nextlevel:
        currlevel = nextlevel
        nextlevel = deque()
        # 把上一次巡回里的nextlevel的所有node导入到currlevel里
        while currlevel:
            node = currlevel.popleft()
            # 把currlevel这一层里所有的node的倒出来，如果有children就放到nextlevel里
            if node.left:
                nextlevel.append(node.left)
                # 这里注意！node的children是存在nextlevel里而不是currlevel，不然这个while会一直循环到tree的地步
            if node.right:
                nextlevel.append(node.right)
        rightside.append(node.val)
        # currlevel里最后一个被倒出来的node就是最右侧的node，存在rightside里
    return rightside

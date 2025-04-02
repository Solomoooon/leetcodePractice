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
    rightside = []
    while nextlevel:
        currlevel = nextlevel
        nextlevel = deque()
        while currlevel:
            node = currlevel.popleft()
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        rightside.append(node.val)

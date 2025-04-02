class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root == None:
        return []
    cur = root
    results = []

    def traverse(cur):
        if cur.left == None and cur.right == None:
            results.append(cur.val)
            return
        if cur.left:
            traverse(cur.left)
        results.append(cur.val)
        if cur.right:
            traverse(cur.right)

    traverse(cur)
    return results

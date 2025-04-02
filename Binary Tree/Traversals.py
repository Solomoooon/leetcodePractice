class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    def preorder(cur):
        if cur is None:
            return
        results.append(cur.val)
        preorder(cur.left)
        preorder(cur.right)

    results = []
    preorder(root)
    return results


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    def traverse(cur):
        if cur is None:
            return
        traverse(cur.left)
        results.append(cur.val)
        traverse(cur.right)

    results = []
    traverse(root)
    return results


def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    def postorder(cur):
        if cur is None:
            return
        postorder(cur.left)
        postorder(cur.right)
        results.append(cur.val)

    results = []
    postorder(root)
    return results

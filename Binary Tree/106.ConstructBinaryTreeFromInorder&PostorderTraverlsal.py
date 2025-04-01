class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def construct(left, right):
        nonlocal postorder_index

        if left > right:
            return None

        root_val = postorder[postorder_index]
        root = TreeNode(root_val)
        postorder_index -= 1

        root.right = construct(inorder_map[root_val] + 1, right)
        # 这道题逻辑和105题是类似的。不过因为是postorder，我们先构建的是right tree然后才是left tree
        root.left = construct(left, inorder_map[root_val] - 1)

        return root

    postorder_index = len(postorder) - 1
    # postorder里最后一位是当前的root，然后依此递减找到新的root

    inorder_map = defaultdict(int)
    for index, value in enumerate(inorder):
        inorder_map[value] = index

    return construct(0, len(postorder) - 1)

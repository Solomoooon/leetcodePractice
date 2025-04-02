class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def construct(left, right):
        nonlocal preorder_index
        if left > right:
            return None

        root_val = preorder[preorder_index]
        # 重点！每一个新的root就是当前preorder list所在的位置，而这个root在inorder里左边的都是left child，右边都是right child
        root = TreeNode(root_val)
        preorder_index += 1

        root.left = construct(left, inorderMap[root_val] - 1)
        # 根据上面的逻辑，root在inordermap左边的node都是left child，右边的都是right child
        root.right = construct(inorderMap[root_val] + 1, right)

        return root

    preorder_index = 0
    # preorder的初始值是0，每次递进1
    inorderMap = defaultdict(int)
    # 这个hashmap是把inorder array invert过来，key是每个node的值，value是他在inorder map里的位置
    for index, value in enumerate(inorder):
        # 这里的enumerate的作用是，index这一位置表示list里的position，value表示inorder[position]
        inorderMap[value] = index

    return construct(0, len(preorder) - 1)

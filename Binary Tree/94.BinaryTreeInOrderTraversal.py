class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# in order traversal is same to sorted list, so the kth smallest is the kth element for in order traversal
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # array for storing in order traversal
    nums = []

    # in order traversal saves in only two circumstances:
    # when a node has no more leafs and if it finishes traversing left or has no left child
    def traverse(cur, num):
        if cur.left == None and cur.right == None:
            nums.append(cur.val)
            return
        if cur.left:
            traverse(cur.left, num)
        nums.append(cur.val)
        if cur.right:
            traverse(cur.right, num)

    traverse(root, 0)
    # With the nums recording the entire sorted tree list, we return the k-1 element as the kth smallest
    return nums[k - 1]

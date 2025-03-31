class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        h = defaultdict(int)
        # 用hashmap记录每个路径值出现的次数

        def traverse(node, curr_sum):
            # preorder traversal
            nonlocal count
            # count记录的是满足targetSum的路径出现的次数
            if node is None:
                return
            curr_sum += node.val
            # 当前sum等于之前的sum +当前node的值
            if curr_sum == targetSum:
                count += 1
                # 如果当前sum正好等于target，说明当前路径就是target路径之一，count + 1
            count += h[curr_sum - targetSum]
            # 这个非常重要！这个从hashmap查找有多少path能到达targetSum path的初始位置（因为这个target path不一定从root开始）
            h[curr_sum] += 1
            # 到达cur sum的path数量+1
            traverse(node.left, curr_sum)
            traverse(node.right, curr_sum)
            h[curr_sum] -= 1
            # 这个是backtrack，比如我们刚刚记录的是一个node的左child，现在换到右child，但是右child不应该知道左child的cur sum情况，所以要-1

        traverse(root, 0)
        return count

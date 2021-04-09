'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = list()
        queue.append(root)
        depth = 1

        while len(queue) != 0:
            cur_len = len(queue)
            for i in range(cur_len):
                node = queue.pop()
                if node.left == None and node.right == None:
                    return depth
                if node.left != None:
                    queue.insert(0, node.left)
                if node.right != None:
                    queue.insert(0, node.right)

            depth+=1





def init_tree():
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    return node1

if __name__ == '__main__':
    root = init_tree()
    solution = Solution()
    print(solution.minDepth(root))
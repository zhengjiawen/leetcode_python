'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

    3
   / \
  9  20
    /  \
   15   7
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build_my_tree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root_value = preorder[pre_left]
            root_node = TreeNode(root_value)
            in_idx = value2inidx[root_value]
            left_len = in_idx - in_left
            right_len = in_right - in_idx

            root_node.left = build_my_tree(pre_left+1, pre_left+left_len, in_left, in_idx-1)
            root_node.right = build_my_tree(pre_left+left_len+1, pre_right, in_idx+1, in_right)

            return root_node

        value2inidx = {value:i for i, value in enumerate(inorder)}
        root = build_my_tree(0,len(preorder)-1, 0, len(inorder)-1)

        return root

def pre_traverse(root):
    if root is None:
        return
    print(root.val)
    pre_traverse(root.left)
    pre_traverse(root.right)

def in_traverse(root):
    if root is None:
        return
    in_traverse(root.left)
    print(root.val)

    in_traverse(root.right)

if __name__ == '__main__':
    pre_order = [3,9,20,15,7]
    in_order = [9,3,15,20,7]

    solution = Solution()
    root = solution.buildTree(pre_order, in_order)
    pre_traverse(root)
    in_traverse(root)


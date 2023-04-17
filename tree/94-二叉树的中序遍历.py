# March 30, 2023

"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
"""

"""
时间复杂度：O(n)
空间复杂度：O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 定义中序遍历的递归函数，传入的参数为递归调用的一个节点root
    def inorder(self, root):
        if root.left:  # 若左子树不为空，递归调用左子树
            self.inorder(root.left)
        # 将传入的节点root的值，加入成员变量self.inorder_list中
        self.inorder_list.append(root.val)
        if root.right:  # 若右子树不为空，递归调用右子树
            self.inorder(root.right)

    def inorderTraversal(self, root):
        # 排除特殊情况，如果根节点为空，则返回一个空列表
        if root == None:
            return list()
       # 定义一个成员变量self.inorder_list, 用来储存中序遍历的结果
        self.inorder_list = list()
        # 调用递归函数
        self.inorder(root)
        # 返回成员变量inorder_list
        return self.inorder_list



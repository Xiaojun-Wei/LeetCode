# March 30, 2023

"""
给给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[3,2,1]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]
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
    # 定义后序遍历的递归函数，传入的参数为递归调用的一个节点root
    def postorder(self, root):
        if root.left:  # 若左子树不为空，递归调用左子树
            self.postorder(root.left)
        if root.right:  # 若右子树不为空，递归调用右子树
            self.postorder(root.right)
        # 将传入的节点root的值，加入成员变量self.preorder_list中
        self.postorder_list.append(root.val)

    def preorderTraversal(self, root):
        # 排除特殊情况，如果根节点为空，则返回一个空列表
        if root == None:
            return list()
       # 定义一个成员变量self.postorder_list, 用来储存后序遍历的结果
        self.postorder_list = list()
        # 调用递归函数
        self.postorder(root)
        # 返回成员变量inorder_list
        return self.postorder_list



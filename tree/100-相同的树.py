# March 30, 2023

"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


示例 1：
输入：p = [1,2,3], q = [1,2,3]
输出：true

示例 2：
输入：p = [1,2], q = [1,null,2]
输出：false

示例 3：
输入：p = [1,2,1], q = [1,1,2]
输出：false
"""

"""
时间复杂度 = O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        # 对传入的两个节点p和q进行比较
        # 若p和q均为空，两者相等，返回True
        if p is None and q is None:
            return True
        # 若p和q中只有一个节点为空，另一个不为空, 则返回False
        elif p and q is None or p is None and q:
            return False
        # 若p和q均不为空，则比较两个点的值
        else:
            # 若两个节点的值不相等，返回false
            if p.val != q.val:
                return False
            # 若两个节点的值相等，分别递归调用p，q的左子树和右子树
            # 并将结果进行与操作（and）
            else:
                return (self.isSameTree(p.left, q.left) and
                        self.isSameTree(p.right, q.right))

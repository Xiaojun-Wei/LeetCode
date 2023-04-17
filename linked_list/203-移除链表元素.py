# March 29, 2023

"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。


示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]
"""

"""
时间复杂度 = O(n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        # 设置哑节点dummyHead
        dummyHead = ListNode()
        # 哑节点指向头节点head
        dummyHead.next = head
        # 初始化当前节点cur为哑节点
        cur = dummyHead

        # 当cur的下个节点不为空，遍历整个列表
        while (cur.next):
            # 当cur的下个节点的值为val
            # 另cur指向cur的下下个节点
            if cur.next.val == val:
                cur.next = cur.next.next
            # 当cur的下个节点的值不为val
            # 令cur前进，更新为其下个节点
            else:
                cur = cur.next
        return dummyHead.next  # 返回哑节点的下个节点，即头节点


# March 30, 2023

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]
"""

"""
时间复杂度：O(n)
空间复杂度：O(n)
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        # 两个指针，一个指头节点，一个指向空
        cur = head
        pre = None

        while cur:
            # 临时变量temp保存cur的下一个节点
            next = cur.next
            cur.next = pre
            # 将pre和cur前进一位
            pre = cur
            cur = next

        return pre

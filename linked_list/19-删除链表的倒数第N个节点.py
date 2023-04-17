# March 29, 2023

"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
"""

"""思路：双指针
时间复杂度 = O(2n) = O(n)
空间复杂度 = O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        # 确定linked list长度
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        # 创建dummy head
        dummy_head = ListNode(0)
        dummy_head.next = head

        # 找到要被删除的位置
        # 循环结束之后，node指向要删除node的前一个位置
        node = dummy_head
        for _ in range(length-n):
            node = node.next

        # 进行删除
        prev = node
        succ = node.next.next
        prev.next = succ # 把prev node和next node连在一起

        # 返回dummy_head.next而不是head，因为head可能会被删除
        return dummy_head.next


if __name__ == "__main__":
    l1 = ListNode([1,2,3,4,5])
    s = Solution()
    print(s.removeNthFromEnd(head=l1, n=2))






# March 22, 2023

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


""""
time complexity: O(n); space complexity:O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头节点
        self.head = ListNode(data[0])



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0) # 存放结果
        p, q, curr = l1, l2, dummy_head
        carry = 0  # 用来存放进位的信息

        while p or q:  # 只要有ListNode非空的情况下
            # 为了解决两个list不等长的情况
            x = p.val if p else 0
            y = q.val if q else 0

            s = x + y + carry
            carry = s // 10
            s = s % 10
            curr.next = ListNode(s)
            curr = curr.next
            # 如果节点下一位没有取节点
            p = p.next if p else p
            q = q.next if q else q

        if carry:
            curr.next = ListNode(carry)
        return dummy_head.next


if __name__ == "__main__":
    l1 = ListNode([2, 4, 3])
    l2 = ListNode([5, 6, 4])
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))



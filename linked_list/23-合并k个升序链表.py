# March 30, 2023

"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]
"""
import heapq

"""
时间复杂度：O(n*log(k))
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 用MyListNode在ListNode外面包裹一层
class MyListNode:
    def __init__(self, l:ListNode):
        self.l = l

    def __eq__(self, other): # equal
        return self.l.val == other.l.val

    def __lt__(self, other ): # less than
        return self.l.val <= other.l.val


class Solution:
    def mergeKLists(self, lists):
        dummyhead = ListNode(0)
        curr = dummyhead
        # if i说明只在这个heap里面放非空的list
        heap = [MyListNode(i) for i in lists if i]
        # heapify可以把list变成heap的形式
        heapq.heapify(heap)

        # 每次挑出一个元素：
        while heap:
            i = heapq.heappop(heap).l
            # 把listnode的值赋给curr node
            curr.next = ListNode(i.val)
            curr = curr.next
            # 把提出来的listnode的下面的node塞回去
            if i.next:
                heapq.heappush(heap, MyListNode(i.next))

        return dummyhead.next




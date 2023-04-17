"""
给你单链表的头节点head，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""


def reverseList(head):
    # 两个指针，一个指头节点，一个指向空
    cur = head
    pre = None

    while cur:
        # 临时变量temp保存cur的下一个节点
        temp = cur.next
        cur.next = pre
        # 将pre和cur前进一位
        pre = cur
        cur = temp

    return pre

if __name__ == "__main__":
    reverseList([1,2,3,4,5])

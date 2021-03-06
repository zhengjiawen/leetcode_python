'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        self.latter_point = None
        def reverseN(head, N):
            '''
            反转前N个节点
            :param head:
            :param N:
            :return:
            '''
            if N == 1:
                self.latter_point = head.next
                return head
            rev_head = reverseN(head.next, N-1)
            head.next.next = head
            head.next = self.latter_point
            return rev_head

        if not head or not head.next:
            return head

        if left==1:
            return reverseN(head, right-left+1)

        head.next = self.reverseBetween(head.next, left-1, right-1)

        return head

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        '''
        用迭代的方式
        :param head:
        :param left:
        :param right:
        :return:
        '''
        if not head or not head.next:
            return head

        counter = 1
        pre, cur = None, head
        while counter < left:
            counter+=1
            pre = cur
            cur = cur.next
        # cur指向第left个节点，也是反转后的最后一个节点
        last = cur
        # 反转前的一个节点
        pre_last = pre
        while counter <= right and cur:
            counter+=1
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        # last 接反转后的那个节点
        last.next = cur

        if left == 1:
            # 这里的pre是反转的头节点
            return pre
        else:
            pre_last.next = pre
            return head

    def reverseBetween3(self, head: ListNode, left: int, right: int) -> ListNode:
        '''
        用迭代的方式
        :param head:
        :param left:
        :param right:
        :return:
        '''
        def reverseN(head, N=2):
            '''
            反转前N个节点，迭代
            :param head:
            :param N:
            :return:
            '''
            counter = 0
            pre, cur = None, head
            rev_last = cur
            while counter < N:
                counter+=1
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
            rev_last.next = cur
            return pre

        if not head or not head.next:
            return head

        pre, cur = None, head
        counter = 1
        while counter<left:
            pre = cur
            cur = cur.next
            counter+=1

        if left == 1:
            return reverseN(cur, right-left+1)

        pre.next = reverseN(cur, right-left+1)
        return head

def init_list():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    return node1


def traverse(root):
    print(root.val)
    if root.next:
        traverse(root.next)

if __name__ == '__main__':
    solution = Solution()
    root = init_list()

    # traverse(root)
    result_root = solution.reverseBetween3(root, 2,4)
    traverse(result_root)



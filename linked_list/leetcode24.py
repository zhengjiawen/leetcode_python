'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        self.latter_point = None

        def reverseN(head, N=2):
            '''
            反转前N个节点
            :param head:
            :param N:
            :return:
            '''
            if not head:
                return head
            if N == 1 or not head.next:
                self.latter_point = head.next
                return head
            rev_head = reverseN(head.next, N - 1)
            head.next.next = head
            head.next = self.latter_point
            return rev_head

        if not head or not head.next:
            return head

        counter = 1
        while head:
            if counter == 1:
                cur = reverseN(head)
                root = cur
                head = cur.next
            elif counter % 2 == 1:
                head = head.next
            else:
                head.next = reverseN(head.next)
                head = head.next
            counter += 1

        return root

def init_list():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node5

    return node1


def traverse(root):
    print(root.val)
    if root.next:
        traverse(root.next)


if __name__ == '__main__':
    solution = Solution()
    root = init_list()

    # traverse(root)
    result_root = solution.swapPairs(root)
    traverse(result_root)
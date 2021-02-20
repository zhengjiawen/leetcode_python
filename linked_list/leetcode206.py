'''
反转一个单链表。
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        迭代方法
        :param head:
        :return:
        '''
        cur, pre = head, None

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        '''
        递归方法
        :param head:
        :return:
        '''


        if not head or not head.next:
            return head

        root = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return root




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
    result_root = solution.reverseList2(root)

    traverse(result_root)
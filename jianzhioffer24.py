'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head):
            if head == None or head.next == None:
                return head

            new_head = reverse(head.next)
            head.next.next = head
            head.next = None

            return new_head

        return reverse(head)

def init():
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
    if root:
        print(root.val)
        traverse(root.next)

if __name__ == '__main__':
    root = init()
    traverse(root)

    solution = Solution()
    node = solution.reverseList(root)
    traverse(node)
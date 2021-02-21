'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

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

        left = head
        counter = 0
        while left:
            counter+=1
            left = left.next
            if counter>=k:
                break

        if counter<k:
            return head
        else:
            new_head = reverseN(head, k)
            head.next = self.reverseKGroup(left, k)
            return new_head



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
    result_root = solution.reverseKGroup(root,3)
    traverse(result_root)
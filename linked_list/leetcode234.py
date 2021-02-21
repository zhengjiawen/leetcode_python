'''
请判断一个链表是否为回文链表。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        res = list()
        while head:
            res.append(head.val)
            head = head.next

        # left, right = 0, len(res)-1

        # while left<right:
        #     if res[left] != res[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True
        return res==res[::-1]




def init_list():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)

    node1.next = node2
    # node2.next = node3
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
    result_root = solution.isPalindrome(root)
    print(result_root)
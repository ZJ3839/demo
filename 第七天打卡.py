"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        pre = None
        cur = head
        while cur is not None:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        head = pre
        return head


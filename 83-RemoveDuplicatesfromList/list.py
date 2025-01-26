# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        templist=head
        if head is None:
            return None
        while templist is not None and templist.next is not None:
            if templist.val==templist.next.val:
                templist.next=templist.next.next
            else:
                templist=templist.next
        return head
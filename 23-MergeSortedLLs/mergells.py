
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergetwolists(lists[i - 1], lists[i])

        return lists [-1]
    
    def mergetwolists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next





#This code merges k sorted linked lists into one sorted linked list by repeatedly 
# merging two lists at a time. It starts from the first list, merges it with the 
# next, and keeps merging the result with the following list until a single sorted list remains.
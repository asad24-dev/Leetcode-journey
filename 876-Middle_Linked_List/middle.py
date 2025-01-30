def middleNode(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head = slow
        return head
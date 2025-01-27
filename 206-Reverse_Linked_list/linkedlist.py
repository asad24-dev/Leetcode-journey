def reverseList(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previous, current = None, head
        while current !=  None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
        
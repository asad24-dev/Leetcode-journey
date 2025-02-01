def copyRandomList(head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        dummy = head
        mapdict = {}
        while dummy:
            copy = Node(x = dummy.val)
            mapdict[dummy] = copy
            dummy = dummy.next
        dummy = head
        while dummy:
            new = mapdict[dummy]
            new.next = mapdict[dummy.next] if dummy.next else None
            new.random = mapdict[dummy.random] if dummy.random else None
            dummy = dummy.next
        return mapdict[head]